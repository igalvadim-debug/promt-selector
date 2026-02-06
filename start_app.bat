@echo off
setlocal enabledelayedexpansion

REM Initialize Conda
call "%~dp0..\miniconda\Scripts\activate.bat" "%~dp0..\miniconda"

REM Check if environment exists, if not create it
conda info --envs | findstr /C:"prompt-selector-env" >nul
if %errorlevel% neq 0 (
    echo Creating new conda environment 'prompt-selector-env'...
    conda create -y -n prompt-selector-env python=3.10
)

REM Activate the environment
call conda activate prompt-selector-env

REM Install required packages if not already installed
python -c "import gradio" 2>nul
if %errorlevel% neq 0 (
    echo Installing gradio...
    pip install gradio
)

REM Change to the script directory
cd /d "%~dp0"

REM Run the application
echo Starting Prompt Selector Node Generator...
python app.py

REM Keep the window open
pause