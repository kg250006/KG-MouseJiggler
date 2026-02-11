#!/bin/bash
cd "$(dirname "$0")"
python3 -c "import pystray, PIL, Quartz" 2>/dev/null || pip3 install -r requirements.txt
nohup python3 mouse_jiggler.py &>/dev/null &
osascript -e 'tell application "Terminal" to close front window' &
