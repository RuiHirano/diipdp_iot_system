import requests
import sys
sys.path.append('..')
from utils.type import Person, Sensor
import datetime
import json

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


if __name__ == "__main__":
    # change from utils.type import Person, Sensor to from type import Person, Sensor
    print('test line')
    # config取得
    config = json.load(open('./../../config/config.json', 'r'))
    token = config["line"]["line_notify_token"]
    api = config["line"]["line_notify_api"]
    line = LineManager(token, api)
    mock_person = Person(id="0", name="Aさん", age="10",
                             sex="male", sensor=Sensor(id="2", name="センサー1"))
    line.send_fall_info(mock_person)