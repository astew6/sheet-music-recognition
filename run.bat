@echo off

if not exist temp (
    mkdir temp
)
call .venv\Scripts\activate.bat
python -m src.MainWindowGui.MainWindowGui

pause