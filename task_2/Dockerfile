FROM python:3.10-alpine3.17
COPY api ./api
WORKDIR /api
COPY requirements.txt .
RUN apk add ffmpeg
RUN apk add nano
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT sleep 5 \
&& alembic upgrade head \
&& uvicorn server:app --host $api_host --port $api_port --reload