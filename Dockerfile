FROM python:3.10-alpine3.17
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./api ./api
WORKDIR /api
ENTRYPOINT ./manager.py site run