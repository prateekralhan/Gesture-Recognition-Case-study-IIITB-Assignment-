FROM python:3.7

RUN mkdir /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

ENTRYPOINT [ "python", "/app/app.py" ]
#ENTRYPOINT [ "tail", "-f", "/app/app.py" ]
