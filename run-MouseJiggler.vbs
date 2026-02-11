Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get the directory where this script is located
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Set the working directory to the script's location
WshShell.CurrentDirectory = scriptDir

' Install dependencies if not already installed
WshShell.Run "cmd /c python -c ""import pystray, PIL"" 2>nul || pip install -r """ & scriptDir & "\requirements.txt""", 0, True

' Run pythonw with full path to the Python script
WshShell.Run "pythonw """ & scriptDir & "\mouse_jiggler.py""", 0, False
