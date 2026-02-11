@echo off
cd /d "%~dp0"
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Done! You can now run the mouse jiggler with run.bat
pause
