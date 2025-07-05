# syntax=docker/dockerfile:1

FROM python:3.12

RUN pip install poetry

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME="opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

ENTRYPOINT python3 run.py

