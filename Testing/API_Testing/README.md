python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install pytest
python -m pip install fastapi httpx pytest

python -m pytest --version

python -m pytest -v