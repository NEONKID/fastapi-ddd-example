FROM python:3.9.5-slim
MAINTAINER N.K

RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /usr/src/app
COPY ./pyproject.toml .
RUN poetry install --no-dev

COPY . .

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--loop=uvloop", "--port=5000"]