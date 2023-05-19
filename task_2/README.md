# Task 1

## To run project with docker compose ver. 2
#### NOTICE: before you run code below, you need paste data instead dotes
```bash
cd task_2
echo "POSTGRES_DB=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...

api_host=0.0.0.0
api_port=8000
external_port=80

SYNC_SQLALCHEMY_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
ASYNC_SQLALCHEMY_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
" >> .env
docker compose up -d
```

## Examples
### Create user
```bash
curl -X POST -d "name=vasya" http://127.0.0.1:80/user/create
```
### Ouput
```python
{"id":4,"uuid":"1d307980-121e-4c95-b936-279cf3b69960"}
```

### Add audio
```bash
curl -X POST \
  -F "user_id=4" \
  -F "uuid=1d307980-121e-4c95-b936-279cf3b69960" \
  -F "uploadfile=@/home/igor/Загрузки/file_example_WAV_1MG.wav" \
  http://127.0.0.1:80/record/
```
### Ouput
```python
"http://0.0.0.0:80/record/?id=9bd784d1-5cdd-4f29-b53b-e68358e7804b&user_id=4"
```

### Get audio
```bash
curl -X GET "http://0.0.0.0:80/record/?id=9bd784d1-5cdd-4f29-b53b-e68358e7804b&user_id=4" -o 'new.mp3'
```
