FROM python:3.10-alpine3.17
COPY ./api ./api
WORKDIR /api
COPY .env .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT sleep 20 && alembic upgrade head && uvicorn server:app --host 127.0.0.1 --port 80