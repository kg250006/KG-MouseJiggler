#!/bin/bash
set -e
cd "$(dirname "$0")"

VENV=".venv"
PY="$VENV/bin/python3"
PIP="$VENV/bin/pip"
REQ="requirements.txt"
STAMP="$VENV/.requirements.sha"

if [ ! -x "$PY" ]; then
    python3 -m venv "$VENV"
    "$PIP" install --upgrade pip
    "$PIP" install -r "$REQ"
    shasum -a 256 "$REQ" > "$STAMP"
elif ! "$PY" -c "import pystray, PIL, Quartz" 2>/dev/null; then
    "$PIP" install -r "$REQ"
    shasum -a 256 "$REQ" > "$STAMP"
elif [ ! -f "$STAMP" ] || ! shasum -a 256 -c "$STAMP" --status 2>/dev/null; then
    "$PIP" install -r "$REQ"
    shasum -a 256 "$REQ" > "$STAMP"
fi

nohup "$PY" mouse_jiggler.py &>/dev/null &
osascript -e 'tell application "Terminal" to close front window' &
