# diipdp_iot_system
IoT Serve and Notify System for DII Product Development Practice

# Requirements
Docker(optional)
Line API token
Python3.7

# Getting Started

## Setup
### 1.Clone Repository
```
$ git clone https://github.com/RuiHirano/diipdp_iot_system.git
```
### 2.Set Line API Token
/config/config.empty.json
```/config/config.empty.json
{
    "line": {
        "line_notify_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "line_notify_api": "https://notify-api.line.me/api/notify"
    }
}
```
### 3.Rename Config File Name
「config.empty.json」→「config.json」

## Use in Local
```
$ cd diipdp_iot_system
$ pip install -r requirements.txt
$ python app.py
```

## Use in Docker
```
$ cd diipdp_iot_system
$ bash docker_build.sh
$ bash docker_run.sh
```
