#!/bin/bash
# Instala dependências do sistema necessárias para FreeTDS e ODBC
apt-get update
apt-get install -y unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc

# Instala as dependências do Python
pip install --no-cache-dir  -r requirements.txt

# (Opcional) Coleta arquivos estáticos, se necessário
python manage.py collectstatic --noinput