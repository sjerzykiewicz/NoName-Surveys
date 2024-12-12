## Prerequisites

In order to use this app, you need to have both `poetry` and `make` installed.

### Poetry

`poetry` is a package manager we're using. You can check the installation instructions [here](https://python-poetry.org/docs/#installing-with-the-official-installer). You should avoid installing `poetry` through `pip` as it is a system-level tool, separated from the `Python` runtime you're currently using. It enables us to treat `Python` as any other dependency and pin its version in `pyproject.toml`.

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### make

`make` is a utility tool that enables us to create aliases for commands we type in the console to run programs. It's much more efficient to use `make` so you don't have to memorize console commands. You can also expose your project's CLI via `Makefile`.

`make` should be available on most Linux distributions.

If you're using Windows, I would get [choco](https://chocolatey.org/install) first, then get `make` from `choco` package gallery.

```sh
choco install make
```

Mac users can pull it using `Homebrew`.

```sh
brew install make
```

## Getting started

To start your work, you need to set up your local environment and hooks.

```sh
make install_dev
```

To quickly format your repo while coding run:

```sh
make format  # isort black flake8
```

Before you commit, always run a full check:

```sh
make build  # pre_commit mypy test
```

## Running the app

If you want to run app locally, you can use:

```sh
make run # poetry run uvicorn src.main:app --reload
```

## Running the tests
To run tests, you can use:
```sh
make test # poetry run pytest
```

or if you want to run tests with coverage:
```sh
make test_cov # poetry run pytest --cov
```
