FROM python:3.7

WORKDIR /usr/src/app

COPY requeriments.txt requeriments.txt

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

EXPOSE 5000


CMD ["python", "/app.py", "-m", "flask", "run", "--host=0.0.0.0"]