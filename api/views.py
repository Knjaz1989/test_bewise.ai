import requests


def get_questions(questions_num: int):
    while True:
        questions = requests.get(
            'https://jservice.io/api/random', params={'count': questions_num}
        ).json()
        for question in questions:
            pass
        break