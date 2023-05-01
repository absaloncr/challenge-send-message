
FROM python:3.9-slim-buster

WORKDIR /app

COPY requeriments.txt .

RUN apt-get update && apt-get install -y python3
RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

ENV FLASK_APP=/src/app.py

EXPOSE 5000

CMD ["python", "-m" "flask", "run", "--host=0.0.0.0"]
