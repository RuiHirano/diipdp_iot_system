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
            '/acceleration', '/acceleration', self.store_acceleration, methods=["POST"])
        self.app.run(debug=True)

    def hello(self):
        name = "Hello World"
        print(name)
        return name

    def send_to_line(self):
        # 転倒検知
        mock_person = Person(id="0", name="Aさん", age="10",
                             sex="male", sensor=Sensor(id="2", name="センサー1"))
        print('send')
        self.line.send_person_concerned(mock_person)

    def detect_fall(self, data) -> bool:
        x = data['x']
        y = data['y']
        z = data['z']
        if abs(x) > 0.8 and abs(y) > 0.8 and abs(z) > 0.8:
            # x, y, zが共に0.8以上であれば転倒
            print('Detact Fall!')
            return True
        return False

    # 加速度を受信する
    def store_acceleration(self):
        data = request.get_json()
        print("acceleration: ",data)
        isFall = self.detect_fall(data)
        if isFall:
            self.send_to_line()
        return "ok"


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
