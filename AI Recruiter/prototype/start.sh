#!/usr/bin/env bash
# AuditReady - Working Demo - launcher
# Starts a single Python process that serves the SPA AND proxies the Azure
# OpenAI API on /api/analyze (so the API key never leaves the server).
#
# If Azure OpenAI is not configured in the workspace .env, the Live Demo page
# automatically falls back to its in-browser deterministic scorer.

set -e

PORT="${PORT:-5173}"
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

echo ""
echo "  +----------------------------------------------------------+"
echo "  |  AuditReady - Working Demo                               |"
echo "  |  http://localhost:${PORT}                                       |"
echo "  |                                                          |"
echo "  |  Pages:                                                  |"
echo "  |    * Live Demo  <- paste JD + resume, run pipeline       |"
echo "  |    * Dashboard                                           |"
echo "  |    * AI Agents                                           |"
echo "  |    * Candidates                                          |"
echo "  |    * Bias Audit (LL144)   <- the moat                    |"
echo "  |    * Compliance                                          |"
echo "  |    * 10 reasons for Sedna  <- strategic close            |"
echo "  |                                                          |"
echo "  |  Press Ctrl+C to stop.                                   |"
echo "  +----------------------------------------------------------+"
echo ""

exec python3 "$HERE/server.py" "$PORT"
