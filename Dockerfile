FROM python:3.9-slim-buster

WORKDIR /app


COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py", "-m", "flask", "run", "--host=0.0.0.0"]