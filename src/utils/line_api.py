import requests
from utils.type import Person
import sys
sys.path.append('..')
import datetime

class LineManager():
    def __init__(self, token, api):
        self.token = token
        self.api = api

    def send_fall_info(self, person: Person):
        message = "\n転倒を検知しました。" \
            + "\n[詳細情報]" \
            + "\n日付: " + datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')\
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
