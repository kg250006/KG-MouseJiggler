@echo off
cd /d "%~dp0"
python -c "import pystray, PIL" 2>nul || pip install -r requirements.txt
python mouse_jiggler.py
