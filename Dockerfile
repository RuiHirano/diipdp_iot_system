FROM python:3.7.8-slim-buster
LABEL maintainer "Rui Hirano <ruirui@ucl.nuee.nagoya-u.ac.jp>"

ENV USERNAME guest
WORKDIR /home/$USERNAME/diidpd_iot_system
COPY . .
RUN pip install -r requirements.txt

WORKDIR /home/$USERNAME/diidpd_iot_system/src
CMD ["python", "app.py"]