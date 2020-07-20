from typing import List, NamedTuple, Dict
from utils.line import LineManager
from utils.type import Person, Sensor
import json
from flask import Flask, Response, jsonify, request


class FlaskServer():
    def __init__(self, line):
        self.app = Flask(__name__)
        self.line = line

    def run(self):
        self.app.add_url_rule('/', '/', self.hello)
        self.app.add_url_rule(
            '/store_data', '/store_data', self.store_data, methods=["POST"])
        self.app.run(debug=True)

    def hello(self):
        name = "Hello World"
        print(name)
        return name

    def send_fall_info(self):
        # 転倒検知
        mock_person = Person(id="0", name="Aさん", age="10",
                             sex="male", sensor=Sensor(id="2", name="センサー1"))
        print('send')
        self.line.send_person_concerned(mock_person)

    def detect_fall(self) -> bool:
        isFall = False
        # 分析結果、転倒だった
        isFall = True
        return isFall

    # 受信機から加速度が送られ、

    def store_data(self):
        print(request.get_json())
        name = "Good"
        print(name)
        isFall = self.detect_fall()
        if isFall:
            self.send_fall_info()
        return name


if __name__ == "__main__":
    print("starting...")

    # config取得
    config = json.load(open('./../config/config.json', 'r'))

    # インスタンス作成
    # Line
    token = config["line"]["line_notify_token"]
    api = config["line"]["line_notify_api"]
    line = LineManager(token, api)

    # Server
    # app.run(debug=True)
    server = FlaskServer(line)
    server.run()
