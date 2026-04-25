#!/usr/bin/env python3
"""
AuditReady working-demo server.

Serves the static SPA (index.html) AND proxies /api/analyze to Azure OpenAI
so the Live Demo page can run real LLM-powered candidate analysis without
exposing the API key to the browser.

- Single-file: only Python stdlib. No pip installs.
- Reads Azure OpenAI credentials from a .env file in this folder, the parent,
  or the great-grandparent (so the demo works whether you run it from
  SAP/prototype, SAP/, or the workspace root).
- If Azure OpenAI is not configured, /api/analyze returns 503 and the
  frontend gracefully falls back to its in-browser deterministic scorer.

Run:    python3 server.py [PORT]   (default 5173)
"""

from __future__ import annotations

import json
import os
import re
import socket
import sys
import time
import traceback
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Optional

HERE = Path(__file__).resolve().parent

# --------------------------------------------------------------------------- #
# .env loader (no python-dotenv dependency)
# --------------------------------------------------------------------------- #
def load_dotenv() -> Optional[Path]:
    """Walk up from this file looking for a .env; load lines into os.environ."""
    for parent in [HERE, *HERE.parents]:
        env_path = parent / ".env"
        if env_path.exists():
            try:
                for raw in env_path.read_text(encoding="utf-8").splitlines():
                    line = raw.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, _, v = line.partition("=")
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    os.environ.setdefault(k, v)
            except Exception:
                pass
            return env_path
    return None


ENV_PATH = load_dotenv()

AZURE_ENDPOINT = (os.environ.get("AZURE_OPENAI_ENDPOINT") or "").rstrip("/")
AZURE_DEPLOYMENT = (
    os.environ.get("AZURE_OPENAI_DEPLOYMENT_GPT4")
    or os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    or ""
)
AZURE_VERSION = os.environ.get("AZURE_OPENAI_VERSION") or "2024-02-15-preview"
AZURE_KEY = os.environ.get("AZURE_OPENAI_KEY") or ""
AZURE_CONFIGURED = bool(AZURE_ENDPOINT and AZURE_DEPLOYMENT and AZURE_KEY)

MAX_INPUT_CHARS = 12000
LLM_TIMEOUT_S = 60


# --------------------------------------------------------------------------- #
# Prompt
# --------------------------------------------------------------------------- #
SYSTEM_PROMPT = """You are an expert recruiting AI used by an independent third-party AEDT bias auditor (NYC Local Law 144 compliant).

Given a JOB DESCRIPTION and a CANDIDATE RESUME, return ONLY a single JSON object (no preamble, no markdown fence) with this exact shape:

{
  "score": <integer 0-100>,
  "match_percent": <integer 0-100>,
  "recommendation": "Strong proceed" | "Proceed" | "Borderline - recruiter review" | "Likely decline",
  "headline": "<one short sentence describing the candidate>",
  "rationale": "<2-3 sentences explaining the decision in plain English>",
  "matched_skills": [<lowercase strings>],
  "missing_skills": [<lowercase strings>],
  "bonus_skills": [<lowercase strings, candidate has but JD did not require>],
  "score_breakdown": [
    {"label": "Skills match",       "got": <int>, "max": 55, "detail": "<short>"},
    {"label": "Years of experience","got": <int>, "max": 25, "detail": "<short>"},
    {"label": "Location fit",       "got": <int>, "max": 8,  "detail": "<short>"},
    {"label": "Level match",        "got": <int>, "max": 7,  "detail": "<short>"},
    {"label": "Bonus depth",        "got": <int>, "max": 5,  "detail": "<short>"}
  ],
  "interview_rubric": [<5 strings, each a tailored interview question>],
  "citations": [
    {"skill": "<lowercase skill>", "snippet": "<<= 120 chars verbatim from resume>"}
  ],
  "fairness_note": "<one sentence reflecting on potential bias risks; for example: 'Candidate uses he/him pronouns; education school not used in scoring; recommend resume-blind screening for the next stage.' Be neutral and audit-aware.>",
  "compensation_recommendation": {
    "base_low": <int USD>,
    "base_mid": <int USD>,
    "base_high": <int USD>,
    "rationale": "<one short sentence>"
  },
  "candidate_meta": {
    "years_experience": <int>,
    "location": "<string>",
    "level": "<string e.g. Senior, Staff>"
  },
  "jd_meta": {
    "years_required": <int>,
    "location": "<string>",
    "level": "<string>"
  }
}

Rules:
- Total of score_breakdown 'got' values must roughly equal "score" (treat 100 as cap).
- Include 4-6 citations. Snippets must come from the resume verbatim.
- Skills should be lowercase short tokens (e.g., "python", "kafka", "ci/cd", "kubernetes", "aws", "successfactors").
- If JD or resume is empty/garbage, still return a valid JSON with score 0 and a clear rationale.
- Never include personally identifying information (PII) beyond what already appears in the inputs.
- Output ONLY the JSON object. No explanation, no fence, no extra text.
"""


def build_messages(jd: str, resume: str) -> list:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"JOB DESCRIPTION\n---\n{jd}\n\n=====\n\nCANDIDATE RESUME\n---\n{resume}",
        },
    ]


def call_azure_openai(jd: str, resume: str) -> Dict[str, Any]:
    url = (
        f"{AZURE_ENDPOINT}/openai/deployments/{AZURE_DEPLOYMENT}/chat/completions"
        f"?api-version={AZURE_VERSION}"
    )
    payload = {
        "messages": build_messages(jd, resume),
        "temperature": 0.2,
        "max_tokens": 2200,
        "top_p": 0.9,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "api-key": AZURE_KEY,
            "User-Agent": "AuditReady-WorkingDemo/1.0",
        },
        method="POST",
    )
    started = time.time()
    with urllib.request.urlopen(req, timeout=LLM_TIMEOUT_S) as resp:
        raw = resp.read()
    elapsed = time.time() - started
    data = json.loads(raw.decode("utf-8"))
    content = data["choices"][0]["message"]["content"]
    parsed = extract_json_object(content)
    parsed.setdefault("_meta", {})
    parsed["_meta"]["llm_latency_s"] = round(elapsed, 2)
    parsed["_meta"]["model"] = AZURE_DEPLOYMENT
    parsed["_meta"]["api_version"] = AZURE_VERSION
    if isinstance(data.get("usage"), dict):
        parsed["_meta"]["tokens"] = data["usage"]
    return parsed


def extract_json_object(text: str) -> Dict[str, Any]:
    """Extract the first balanced JSON object from a possibly noisy LLM reply."""
    if not text:
        raise ValueError("Empty LLM response")
    # Strip markdown code fences if present
    fence = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", text)
    candidate = fence.group(1) if fence else None
    if candidate is None:
        # find the first { ... matching } using a simple bracket scanner
        start = text.find("{")
        if start < 0:
            raise ValueError("No JSON object found in LLM response")
        depth = 0
        end = -1
        in_str = False
        esc = False
        for i, ch in enumerate(text[start:], start=start):
            if esc:
                esc = False
                continue
            if ch == "\\" and in_str:
                esc = True
                continue
            if ch == '"':
                in_str = not in_str
                continue
            if in_str:
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        if end < 0:
            raise ValueError("Unterminated JSON object in LLM response")
        candidate = text[start : end + 1]
    return json.loads(candidate)


# --------------------------------------------------------------------------- #
# Server
# --------------------------------------------------------------------------- #
class Handler(BaseHTTPRequestHandler):
    server_version = "AuditReadyDemo/1.0"

    # ------- helpers -------
    def _send_json(self, code: int, payload: Dict[str, Any]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path) -> None:
        try:
            data = path.read_bytes()
        except FileNotFoundError:
            self.send_error(404, "Not Found")
            return
        ctype = guess_ctype(path)
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        if path.suffix == ".html":
            self.send_header("Cache-Control", "no-cache")
        else:
            self.send_header("Cache-Control", "public, max-age=300")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt: str, *args: Any) -> None:
        # Quieter than default; redact api keys defensively (none should appear).
        msg = fmt % args
        sys.stderr.write(f"[{time.strftime('%H:%M:%S')}] {self.address_string()} {msg}\n")

    # ------- routes -------
    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path == "/api/health":
            self._send_json(
                200,
                {
                    "ok": True,
                    "azure_configured": AZURE_CONFIGURED,
                    "deployment": AZURE_DEPLOYMENT if AZURE_CONFIGURED else None,
                    "api_version": AZURE_VERSION if AZURE_CONFIGURED else None,
                    "endpoint_host": (
                        AZURE_ENDPOINT.split("//", 1)[-1] if AZURE_CONFIGURED else None
                    ),
                    "env_loaded_from": str(ENV_PATH) if ENV_PATH else None,
                },
            )
            return
        # static
        rel = path.lstrip("/") or "index.html"
        target = (HERE / rel).resolve()
        # Prevent path traversal
        try:
            target.relative_to(HERE)
        except ValueError:
            self.send_error(403, "Forbidden")
            return
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            target = HERE / "index.html"
        self._send_file(target)

    def do_POST(self) -> None:
        path = self.path.split("?", 1)[0]
        if path != "/api/analyze":
            self.send_error(404, "Not Found")
            return
        if not AZURE_CONFIGURED:
            self._send_json(
                503,
                {
                    "error": "azure_not_configured",
                    "message": (
                        "Azure OpenAI credentials are not present in .env. "
                        "Set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT, "
                        "AZURE_OPENAI_VERSION, and AZURE_OPENAI_KEY."
                    ),
                },
            )
            return
        try:
            length = int(self.headers.get("Content-Length", "0") or "0")
        except ValueError:
            length = 0
        if length > 200_000:  # ~200KB request cap
            self._send_json(413, {"error": "payload_too_large"})
            return
        try:
            raw = self.rfile.read(length) if length else b"{}"
            body = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            self._send_json(400, {"error": "invalid_json"})
            return
        jd = (body.get("jd") or "").strip()[:MAX_INPUT_CHARS]
        resume = (body.get("resume") or "").strip()[:MAX_INPUT_CHARS]
        if not jd or not resume:
            self._send_json(
                400, {"error": "missing_inputs", "message": "Both 'jd' and 'resume' are required."}
            )
            return
        try:
            result = call_azure_openai(jd, resume)
            self._send_json(200, {"ok": True, "result": result})
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:500]
            except Exception:
                pass
            self._send_json(
                502,
                {
                    "error": "upstream_error",
                    "status": e.code,
                    "message": (
                        f"Azure OpenAI returned HTTP {e.code}. Most likely the "
                        f"deployment name, endpoint, or api-version is wrong, or "
                        f"the key is expired."
                    ),
                    "detail": detail,
                },
            )
        except urllib.error.URLError as e:
            self._send_json(
                504,
                {
                    "error": "upstream_unreachable",
                    "message": (
                        "Could not reach Azure OpenAI. Check network connectivity "
                        "to the endpoint and that the host name is correct."
                    ),
                    "detail": str(e.reason)[:300],
                },
            )
        except (ValueError, json.JSONDecodeError) as e:
            self._send_json(
                502,
                {
                    "error": "llm_parse_error",
                    "message": (
                        "Azure OpenAI returned a response that wasn't valid JSON. "
                        "Falling back to local mode is recommended."
                    ),
                    "detail": str(e)[:300],
                },
            )
        except socket.timeout:
            self._send_json(504, {"error": "timeout", "message": "LLM request timed out."})
        except Exception as e:  # noqa: BLE001 - last-resort
            traceback.print_exc()
            self._send_json(
                500,
                {"error": "internal_error", "message": "Unexpected server error.", "detail": str(e)[:300]},
            )


def guess_ctype(path: Path) -> str:
    ext = path.suffix.lower()
    return {
        ".html": "text/html; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".jsx": "text/javascript; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".ico": "image/x-icon",
        ".map": "application/json; charset=utf-8",
        ".txt": "text/plain; charset=utf-8",
        ".md": "text/markdown; charset=utf-8",
    }.get(ext, "application/octet-stream")


def main() -> None:
    port = 5173
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            sys.stderr.write(f"Bad port '{sys.argv[1]}'. Using {port}.\n")
    bind = "127.0.0.1"
    server = ThreadingHTTPServer((bind, port), Handler)
    azure_msg = (
        f"  Azure OpenAI : {AZURE_DEPLOYMENT} ({AZURE_VERSION}) on {AZURE_ENDPOINT}"
        if AZURE_CONFIGURED
        else "  Azure OpenAI : NOT configured  (Live Demo will fall back to in-browser scoring)"
    )
    env_msg = f"  .env loaded  : {ENV_PATH}" if ENV_PATH else "  .env loaded  : (none found)"
    print("")
    print("  AuditReady - Working Demo")
    print(f"  URL          : http://{bind}:{port}")
    print(env_msg)
    print(azure_msg)
    print("")
    print("  Routes:")
    print("    GET  /            -> index.html (single-file SPA)")
    print("    GET  /api/health  -> JSON: configuration status")
    print("    POST /api/analyze -> JSON: real GPT-4 analysis of {jd, resume}")
    print("")
    print("  Press Ctrl+C to stop.")
    print("")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
