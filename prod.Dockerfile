FROM python:3

RUN mkdir /code

WORKDIR /code
# https://apptension.com/blog/2017/11/09/django-settings-for-multiple-environments/
COPY requirements/ /code/requirements/
# https://hub.docker.com/_/python/
RUN pip install --no-cache-dir -r requirements/production.txt
COPY . /code/