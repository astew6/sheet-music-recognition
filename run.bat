@echo off

if not exist temp (
    mkdir temp
)

if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install --upgrade pip >nul 2>&1
    pip install pygame
    pip install pygame-ce pygame_gui
)

call .venv\Scripts\activate.bat

call .venv\Scripts\activate.bat
python -m src.MainWindowGui.MainWindowGui

pause