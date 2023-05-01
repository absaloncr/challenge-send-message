FROM python:3.9-slim-buster

RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 5000

CMD ["python", "/app/main.py", "-m", "flask", "run", "--host=0.0.0.0"]