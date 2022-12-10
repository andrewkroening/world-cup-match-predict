install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,missing-timeout,redefined-builtin --extension-pkg-whitelist='pydantic' ./logic/*.py streamlit_app.py

format:
	black ./logic/*.py *.py

all: install lint format