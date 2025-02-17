FROM python:3.9-slim

ENV APP_HOME /flask

WORKDIR ${APP_HOME}

# Install system dependencies and necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment inside the container
RUN python3 -m venv /flask/venv

# Activate the virtual environment and install the dependencies
COPY requirements.txt ${APP_HOME}/
RUN /flask/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the app files into the container
COPY app.py cat_responses.py ${APP_HOME}/
COPY templates/ ${APP_HOME}/templates/

# Download the spaCy model
RUN /flask/venv/bin/python -m spacy download en_core_web_sm

EXPOSE 8080

# Run the app inside the virtual environment
CMD ["/flask/venv/bin/python", "app.py"]
