Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get the directory where this script is located
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Set the working directory to the script's location
WshShell.CurrentDirectory = scriptDir

' Run pythonw with full path to the Python script
WshShell.Run "pythonw """ & scriptDir & "\mouse_jiggler.py""", 0, False
