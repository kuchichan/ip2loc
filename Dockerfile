# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY pyproject.toml poetry.lock /code/
RUN pip install poetry && poetry config virtualenvs.create false \
	&& poetry install --no-interaction

COPY . /code/
