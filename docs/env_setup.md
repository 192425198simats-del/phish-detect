# Development Environment Setup

## 1. Python Environment Setup (Windows)
- Ensure Python version is at least 3.10: `python --version`
- Create virtual environment: `python -m venv .venv`
- Activate virtual environment: `.\.venv\Scripts\Activate.ps1`
- Verify activation: check that shell prompt shows `(.venv)` prefix

## 2. Install Core Libraries
```
fastapi
uvicorn
pandas
numpy
scikit-learn
joblib
requests
tldextract
python-whois
dnspython
jupyter

# Future additions
lightgbm  # TODO: confirm usage
xgboost   # TODO: confirm usage
transformers  # Optional for BERT, TODO: evaluate necessity
```

## 3. .gitignore Update
- Include ignores for Python virtual environments (`.venv/`) and cache directories (`__pycache__/`).

## 4. Commands to Run
```
python -m venv .venv
```
```
.\.venv\Scripts\Activate.ps1
```
```
pip install -r requirements.txt
```
