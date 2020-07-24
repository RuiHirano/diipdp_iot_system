import time
import math
import random
import requests

class Sensor():
    def __init__(self):
        pass

    def run(self):
        for i in range(1000):
            x = math.sin(math.radians(360*random.random()))
            y = math.sin(math.radians(360*random.random()))
            z = math.sin(math.radians(360*random.random()))
            print("{}: x: {}, y: {}, z: {}".format(i, x, y, z))
            json_data = {"x": x, "y": y, "z": z}
            self.send_acceleration(json_data)
            time.sleep(1)

    def send_acceleration(self, json_data):
        res = requests.post('http://localhost:5000/acceleration', json=json_data)
        return res


if __name__ == "__main__":
    print("starting...")

    # Sensor
    sensor = Sensor()
    sensor.run()