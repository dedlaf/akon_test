FROM python:3.9

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y sqlite3
RUN pip install --upgrade --no-cache-dir pip && pip install -r requirements.txt

COPY run_uwsgi.sh run_uwsgi.sh
COPY . .

ENTRYPOINT ["bash", "run_uwsgi.sh"]
