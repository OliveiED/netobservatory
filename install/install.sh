#!/bin/bash

apt update

apt install -y \
python3 \
python3-venv \
python3-pip \
postgresql \
postgresql-contrib \
tcpdump \
git

python3 -m venv venv

source venv/bin/activate

pip install -r requirements/requirements.txt
