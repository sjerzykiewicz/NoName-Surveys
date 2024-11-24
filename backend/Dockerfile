FROM python:3.10 AS python-base

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
ENV PATH="/opt/poetry/bin:$PATH"

COPY ./pyproject.toml ./poetry.lock /app/

COPY . .

RUN poetry install --no-root
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
