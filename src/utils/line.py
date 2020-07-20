import requests
from utils.type import Person
import sys
sys.path.append('..')


class LineManager():
    def __init__(self, token, api):
        self.token = token
        self.api = api

    def send_person_concerned(self, person: Person):
        message = "\n転倒を検知しました。" \
            + "\n[詳細情報]" \
            + "\nID: " + person.id \
            + "\n名前: " + person.name \
            + "\n性別: " + person.sex \
            + "\n年齢: " + person.age
        self.send_to_line(message)
        return 0

    def send_to_line(self, message: str):
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + self.token}  # 発行したトークン
        requests.post(self.api, data=payload, headers=headers)
