from enum import Enum
from typing import List, NamedTuple, Dict
from datetime import datetime


class Receiver(NamedTuple):  # 受信機
    id: str                             # id
    name: str                        # センサ名
    place: str                      # 場所名


class Sensor(NamedTuple):   # 送信機
    id: str                             # id
    name: str                        # センサ名


class Person(NamedTuple):   # 該当者情報
    id: str                             # id
    name: str                        # 人名
    age: str                      # 年齢
    sex: str                      # 性別
    sensor: Sensor                 # 所持しているセンサ情報
