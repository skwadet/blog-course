FROM python:3.8-slim-buster

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    g++ \
    libpq-dev \
    && apt-get clean \
    && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

CMD [ "gunicorn", "-c", "python:gunicorn.config", "blog_course.wsgi:application" ]