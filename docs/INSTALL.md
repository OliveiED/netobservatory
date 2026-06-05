1. Clonar projeto

git clone git@github.com:OliveiED/netobservatory.git

2. Instalar dependencias

./install/install.sh

3. Restaurar banco

createdb netobservatory

psql netobservatory < schema.sql

4. Restaurar dados

psql netobservatory < netobservatory.sql

5. Iniciar collector

python -m collectors.dns_collector
