# Task 1

## To run project with docker compose ver. 2
#### NOTICE: before you run code below, you need paste data instead dotes
```bash
cd task_1
echo "POSTGRES_DB=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...

SYNC_SQLALCHEMY_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
ASYNC_SQLALCHEMY_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
" >> .env
docker compose up -d
```

## Examples
### With count 1
```bash
curl -X POST -d "questions_num=1" http://127.0.0.1:80/
```
#### data
```python
[{'airdate': '1994-03-15T19:00:00.000Z',
  'answer': 'the Camp David Accords',
  'category': {'clues_count': 139,
               'created_at': '2022-12-30T18:40:25.945Z',
               'id': 959,
               'title': 'the 20th century',
               'updated_at': '2022-12-30T18:40:25.945Z'},
  'category_id': 959,
  'created_at': '2022-12-30T18:51:56.346Z',
  'game_id': 6638,
  'id': 34666,
  'invalid_count': None,
  'question': 'Name given the 2 Israeli-Egyptian agreements signed in the U.S. '
              'Sept. 17, 1978',
  'updated_at': '2022-12-30T18:51:56.346Z',
  'value': 200}]
```
#### ouput
```python
{}
```

### With count 2
```bash
curl -X POST -d "questions_num=2" http://127.0.0.1:80/
```
#### data
```python
[{'airdate': '1994-03-15T19:00:00.000Z',
  'answer': 'the Camp David Accords',
  'category': {'clues_count': 139,
               'created_at': '2022-12-30T18:40:25.945Z',
               'id': 959,
               'title': 'the 20th century',
               'updated_at': '2022-12-30T18:40:25.945Z'},
  'category_id': 959,
  'created_at': '2022-12-30T18:51:56.346Z',
  'game_id': 6638,
  'id': 34666,
  'invalid_count': None,
  'question': 'Name given the 2 Israeli-Egyptian agreements signed in the U.S. '
              'Sept. 17, 1978',
  'updated_at': '2022-12-30T18:51:56.346Z',
  'value': 200},
 {'airdate': '1989-05-09T19:00:00.000Z',
  'answer': 'Texas',
  'category': {'clues_count': 5,
               'created_at': '2022-12-30T18:43:21.071Z',
               'id': 1638,
               'title': 'college nicknames',
               'updated_at': '2022-12-30T18:43:21.071Z'},
  'category_id': 1638,
  'created_at': '2022-12-30T18:43:21.104Z',
  'game_id': 4632,
  'id': 14116,
  'invalid_count': None,
  'question': 'Longhorns',
  'updated_at': '2022-12-30T18:43:21.104Z',
  'value': 100}]
```
#### ouput
```python
[{'airdate': '1994-03-15T19:00:00.000Z',
  'answer': 'the Camp David Accords',
  'category': {'clues_count': 139,
               'created_at': '2022-12-30T18:40:25.945Z',
               'id': 959,
               'title': 'the 20th century',
               'updated_at': '2022-12-30T18:40:25.945Z'},
  'category_id': 959,
  'created_at': '2022-12-30T18:51:56.346Z',
  'game_id': 6638,
  'id': 34666,
  'invalid_count': None,
  'question': 'Name given the 2 Israeli-Egyptian agreements signed in the U.S. '
              'Sept. 17, 1978',
  'updated_at': '2022-12-30T18:51:56.346Z',
  'value': 200}]
```

### With count 3
```bash
curl -X POST -d "questions_num=3" http://127.0.0.1:80/
```
#### data
```python
[{'airdate': '1994-03-15T19:00:00.000Z',
  'answer': 'the Camp David Accords',
  'category': {'clues_count': 139,
               'created_at': '2022-12-30T18:40:25.945Z',
               'id': 959,
               'title': 'the 20th century',
               'updated_at': '2022-12-30T18:40:25.945Z'},
  'category_id': 959,
  'created_at': '2022-12-30T18:51:56.346Z',
  'game_id': 6638,
  'id': 34666,
  'invalid_count': None,
  'question': 'Name given the 2 Israeli-Egyptian agreements signed in the U.S. '
              'Sept. 17, 1978',
  'updated_at': '2022-12-30T18:51:56.346Z',
  'value': 200},
 {'airdate': '1989-05-09T19:00:00.000Z',
  'answer': 'Texas',
  'category': {'clues_count': 5,
               'created_at': '2022-12-30T18:43:21.071Z',
               'id': 1638,
               'title': 'college nicknames',
               'updated_at': '2022-12-30T18:43:21.071Z'},
  'category_id': 1638,
  'created_at': '2022-12-30T18:43:21.104Z',
  'game_id': 4632,
  'id': 14116,
  'invalid_count': None,
  'question': 'Longhorns',
  'updated_at': '2022-12-30T18:43:21.104Z',
  'value': 100},
 {'airdate': '1995-10-23T19:00:00.000Z',
  'answer': 'the Empire State Building',
  'category': {'clues_count': 45,
               'created_at': '2022-12-30T18:43:42.655Z',
               'id': 1708,
               'title': 'the 1930s',
               'updated_at': '2022-12-30T18:43:42.655Z'},
  'category_id': 1708,
  'created_at': '2022-12-30T18:55:48.240Z',
  'game_id': 7095,
  'id': 43481,
  'invalid_count': None,
  'question': 'This 102-story New York skyscraper officially opened May 1, '
              '1931',
  'updated_at': '2022-12-30T18:55:48.240Z',
  'value': 100}]
```
#### ouput
```python
{'airdate': '1989-05-09T19:00:00.000Z',
  'answer': 'Texas',
  'category': {'clues_count': 5,
               'created_at': '2022-12-30T18:43:21.071Z',
               'id': 1638,
               'title': 'college nicknames',
               'updated_at': '2022-12-30T18:43:21.071Z'},
  'category_id': 1638,
  'created_at': '2022-12-30T18:43:21.104Z',
  'game_id': 4632,
  'id': 14116,
  'invalid_count': None,
  'question': 'Longhorns',
  'updated_at': '2022-12-30T18:43:21.104Z',
  'value': 100}
```