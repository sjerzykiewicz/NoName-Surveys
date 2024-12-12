# Installation
install_venv:
	poetry install --no-root

install_pre_commit:
	poetry run pre-commit install

# Dev tools
codespell:
	poetry run codespell

isort:
	poetry run isort src

black:
	poetry run black --config pyproject.toml src

pyupgrade:
	poetry run pyupgrade --py36-plus

yesqa:
	poetry run yesqa

# pre-commit flake8 runs only against staged files
flake8:
	poetry run flake8 src

ruff:
	poetry run ruff check src

mypy:
	poetry run mypy --incremental --no-install-types --show-error-codes --pretty src

pre_commit:
	poetry run pre-commit run -a

test:
	poetry run pytest

test_cov:
	poetry run pytest --cov

compile_env:
	poetry lock --no-update

install_dev: install_venv install_pre_commit

format: isort black -py all

lint: pre_commit ruff flake8 mypy

build: pre_commit mypy test

run:
	poetry run uvicorn src.main:app --reload
