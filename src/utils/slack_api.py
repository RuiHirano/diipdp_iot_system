import os
from slack import WebClient
from slack.errors import SlackApiError
from utils.type import Person, Sensor
import datetime
import json

class SlackManager():
    def __init__(self, token):
        self.client = WebClient(token=token)

    def send_fall_info(self, person: Person):
        message = "\n転倒を検知しました。" \
            + "\n[詳細情報]" \
            + "\n日付: " + datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')\
            + "\nID: " + person.id \
            + "\n名前: " + person.name \
            + "\n性別: " + person.sex \
            + "\n年齢: " + person.age

        self.send_to_slack(message)
        return 0

    def send_to_slack(self, message: str):
        response = self.client.chat_postMessage(
            channel='#bot_fall_detection',
            text=message)
        return response


if __name__ == "__main__":
    print('test slackbot')
    # config取得
    config = json.load(open('./../../config/config.json', 'r'))
    token = config["slack"]["slack_access_token"]
    slack = SlackManager(token)
    mock_person = Person(id="0", name="Aさん", age="10",
                             sex="male", sensor=Sensor(id="2", name="センサー1"))
    slack.send_fall_info(mock_person)