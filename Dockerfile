FROM python:3.7

RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 5000

CMD ["python", "/app.py", "-m", "flask", "run", "--host=0.0.0.0"]