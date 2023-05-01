FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 5000

CMD ["python", "app.py", "-m", "flask", "run", "--host=0.0.0.0"]