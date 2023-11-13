FROM python:3.9
COPY app/* /home/
WORKDIR /home
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0