FROM python:3.9-slim-bullseye

WORKDIR /flask-loan-app

COPY artefacts/requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /flask-loan-app/

CMD ["python", "-m", "flask", "--app", "Hello.py", "run", "--host=0.0.0.0", "--port=8000"]