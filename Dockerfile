#Dockerfile, Image, Container
FROM python:3.9

ADD main.py .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./main.py"]