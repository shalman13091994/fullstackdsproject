FROM python:3.8-slim-buster
WORKDIR /service
# COPY requirements.txt .
COPY . /service
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "./Api/manage.py", "runserver", "0.0.0.0:8080"] 

# same port to be used in the aws 