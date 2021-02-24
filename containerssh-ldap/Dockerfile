FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY ./app /app
