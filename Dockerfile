FROM python:3.13.2-slim

RUN apt-get update && apt-get install -y \
  unixodbc \
  unixodbc-dev \
  freetds-dev \
  freetds-bin \
  tdsodbc \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

COPY config/freetds.conf /etc/freetds/freetds.conf

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 10000

CMD ["gunicorn", "--bind", "0.0.0.0:10000", "setup.wsgi:application"]