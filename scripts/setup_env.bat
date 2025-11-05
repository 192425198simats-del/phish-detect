@echo off
setlocal

REM Check if Python is available
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not on PATH. Please install Python 3.10 or higher.
    exit /b 1
)

REM Verify Python version is 3.10+
python -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)"
if %errorlevel% neq 0 (
    echo Python 3.10 or higher is required. Current version:
    python --version
    exit /b 1
)

REM Create virtual environment if missing
if not exist "venv\Scripts\python.exe" (
    echo Creating virtual environment in .\venv ...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Failed to create the virtual environment.
        exit /b 1
    )
)

REM Activate virtual environment
call venv\Scripts\activate
if not defined VIRTUAL_ENV (
    echo Unable to activate the virtual environment.
    exit /b 1
)

echo Upgrading pip...
python -m pip install --upgrade pip

REM Install from requirements.txt if present
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    python -m pip install -r requirements.txt
) else (
    echo requirements.txt not found. Skipping requirements installation.
)

echo Installing core project libraries...
python -m pip install jupyter fastapi uvicorn scikit-learn pandas numpy requests joblib dnspython tldextract python-whois

echo.
echo ✅ Environment setup complete

endlocal
