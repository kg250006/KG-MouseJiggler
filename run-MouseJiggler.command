#!/bin/bash
cd "$(dirname "$0")"
nohup python3 mouse_jiggler.py &>/dev/null &
osascript -e 'tell application "Terminal" to close front window' &
