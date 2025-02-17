FROM python:3.9-slim

ENV APP_HOME /flask

WORKDIR ${APP_HOME}

COPY requirements.txt app.py cat_responses.py ${APP_HOME}/
COPY templates/ ${APP_HOME}/templates/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080


CMD ["python", "app.py"]
