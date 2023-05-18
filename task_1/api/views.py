import requests
from fastapi import Depends, Form

from database.base_handlers import save_question
from database.db_sync import get_session


async def get_questions(questions_num: int = Form(), session=Depends(get_session)):
    pre_last = {}
    while True:
        questions = requests.get(
            'https://jservice.io/api/random', params={'count': questions_num}
        ).json()
        from pprint import pprint
        for num, question in enumerate(questions):
            data = {
                'id': question['id'],
                'question': question['question'],
                'answer': question['answer'],
                'created_date': question['created_at'],
            }
            if not await save_question(session, data):
                continue
            questions_num -= 1
            if questions_num != 0:
                pre_last = question
            else:
                return pre_last
