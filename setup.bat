@echo off
title TV Sales Analysis Setup

echo ================================
echo  CLEAN PROJECT SETUP STARTING
echo ================================

REM 1. Create virtual environment
echo [1/5] Creating virtual environment...
python -m venv venv

REM 2. Activate venv
echo [2/5] Activating environment...
call venv\Scripts\activate

REM 3. Upgrade pip
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip

REM 4. Install dependencies
echo [4/5] Installing requirements...
pip install -r requirements.txt

REM 5. Done
echo ================================
echo  SETUP COMPLETE SUCCESSFULLY
echo ================================

echo.
echo Starting Streamlit app...
echo ================================

REM 6. Run dashboard
python -m streamlit run dashboard/app.py

pause