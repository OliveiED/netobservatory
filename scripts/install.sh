#!/bin/bash

set -e

echo "[1/7] Instalando dependências"

apt update

apt install -y \
python3 \
python3-venv \
python3-pip \
postgresql \
postgresql-contrib \
git \
tcpdump

echo "[2/7] Criando ambiente virtual"

python3 -m venv venv

source venv/bin/activate

echo "[3/7] Instalando bibliotecas"

pip install -r requirements.txt

echo "[4/7] Criando banco"

sudo -u postgres psql <<EOF
CREATE USER netobservatory WITH PASSWORD 'netobservatory';
CREATE DATABASE netobservatory OWNER netobservatory;
EOF

echo "[5/7] Aplicando schema"

psql -U netobservatory \
     -d netobservatory \
     -f sql/schema.sql

echo "[6/7] Instalando serviço"

cp systemd/netobservatory-dns.service \
   /etc/systemd/system/

systemctl daemon-reload

echo "[7/7] Habilitando serviço"

systemctl enable netobservatory-dns

echo "Instalação concluída."
