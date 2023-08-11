FROM docker.io/python:3.8-buster

WORKDIR /opt/cshhacks

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY hackathon/ hackathon/
COPY migrations/ migrations/
COPY templates/ templates/
COPY *.py .

COPY dev.sh .

#ENTRYPOINT ["/bin/bash", "dev.sh"]
ENTRYPOINT ["gunicorn", "hackathon:app", "--bind=0.0.0.0:8080", "--access-logfile=-"]