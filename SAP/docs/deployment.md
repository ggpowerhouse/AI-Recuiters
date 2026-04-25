# Deploying the AuditReady working demo

The prototype is a single, self-contained `index.html` (~123 KB). All libraries (React, Tailwind, Recharts, Lucide, Babel) are loaded from CDN. No build step. No backend. No environment variables. No `/api` calls. The Live Demo (JD + resume → 6-agent pipeline → audit log) runs **entirely in the browser**, so the file is fully usable offline once a browser has loaded the CDN libraries.

That means you can:

- **Open it directly** by double-clicking the file (it opens with `file://` and runs).
- **Host it anywhere** a static file lives — the live demo URL becomes a real, shareable link.
- **Email/Slack the file** (123 KB) to anyone — they can open it in any modern browser.

The single file you need is at:

```
/Users/gauravgolchha/Downloads/ppg/SAP/prototype/index.html
```

There are five good deployment options. Pick the one that matches your audience.

---

## 1. Lovable (best for "I want to keep iterating on it with AI")

Best for: deploying instantly and then editing the demo with natural-language prompts.

1. Open <https://lovable.dev> and sign in.
2. Click **New Project** → **Import code** (or **Start from scratch**).
3. When prompted for code/files, **paste the entire contents of `index.html`** into the editor as the project's single source file (or upload it if Lovable asks for a file).
4. Tell Lovable: *"This is a self-contained static HTML demo. Use this exact file as `index.html`. Don't rebuild it — just deploy it."*
5. Click **Publish**. Lovable gives you a `*.lovable.app` URL.
6. To iterate, prompt Lovable directly: *"Change the Cost per Hire on the dashboard to $750"*, *"Add a new agent called Reference Checker"*, etc. Lovable will edit the inline JSX inside `index.html`.

> Lovable is a code-gen tool. Because the file is one HTML with no build step, Lovable treats it as a flat asset — which is exactly what you want.

---

## 2. Netlify Drop (fastest — 30 seconds, no account required)

Best for: showing the demo to a senior, in their inbox, today.

1. Open <https://app.netlify.com/drop>.
2. Drag the `prototype/` folder (the one containing `index.html`) onto the page.
3. Netlify gives you a public URL like `https://chipper-pony-12ab34.netlify.app`.
4. Optionally, sign in to claim the site and add a custom subdomain like `auditready-demo.netlify.app`.

That URL is now live. No CLI. No git. No account required to create the link.

> The free tier includes HTTPS by default and unlimited deploys for static sites of this size.

---

## 3. Vercel (best for "make it look like a real product")

Best for: a polished URL like `auditready.vercel.app`, with HTTPS and a real CDN.

1. Open <https://vercel.com/new>.
2. Click "Continue with GitHub" (or sign in however you prefer).
3. Click "Import Project" → "Deploy without a Git repo" → drag the `prototype/` folder.
4. Vercel gives you `https://<project>.vercel.app`. First deploy takes ~30 seconds.
5. To make it production: Settings → Domains → add a custom subdomain.

> If you'd rather use the CLI: `npx vercel deploy --prod ./prototype` (requires Node + the Vercel CLI).

---

## 4. GitHub Pages (best if your firm has an org GitHub already)

Best for: long-lived demo at `<org>.github.io/auditready-demo`.

```bash
cd /Users/gauravgolchha/Downloads/ppg/SAP/prototype
git init
git add index.html
git commit -m "AuditReady working demo"
# create a repo on github.com first (any name, e.g. auditready-demo)
git branch -M main
git remote add origin https://github.com/<your-org>/auditready-demo.git
git push -u origin main
```

Then on github.com:

1. Repo → **Settings** → **Pages**.
2. **Source**: Deploy from a branch.
3. **Branch**: `main`, folder `/ (root)`.
4. Save. After a minute, your demo is live at `https://<your-org>.github.io/auditready-demo/`.

This is the right home for a demo that needs to live for weeks during a sales cycle. It's free, it's HTTPS, and it lives next to the source.

---

## 5. Cloudflare Pages (best for a private/staging URL)

Best for: putting the demo behind a Cloudflare Access policy if you want to share it only with named people.

1. Go to <https://dash.cloudflare.com> → **Workers & Pages** → **Create application** → **Pages** → **Upload assets**.
2. Drag the `prototype/` folder.
3. Cloudflare gives you `https://<project>.pages.dev`.
4. Optional: **Settings → Access policies** to require Google/Okta SSO before viewing the demo.

This is the right home if the demo includes anything you don't want indexed by Google. (The included `<meta name="robots" content="noindex" />` tag also helps.)

---

## 6. Local-only (zero deployment — for the conference room)

If you just want to show it on a laptop and screen-share:

```bash
cd /Users/gauravgolchha/Downloads/ppg/SAP/prototype
python3 -m http.server 5173
```

Open <http://localhost:5173>. That's it. The included `start.sh` does the same with one command.

---

## Sanity checks before the demo

- Open the live URL on the laptop you'll be presenting from. CDN cold-starts can take a second the first time.
- Do one full Live Demo run with the sample JD/resume so the user-flow is muscle memory before the real demo.
- Confirm the **Why this fits** page loads — that's the slide that does the selling.
- (Optional) Take a screenshot of the LL144 audit page in case the live demo room has flaky wifi.

## Updating the live demo

Single file. To update, replace `index.html` and redeploy with the same drag-and-drop. Browsers may cache aggressively — append `?v=2` to the URL the first time you share an updated version.
