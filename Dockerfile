FROM python:3.7-slim
RUN apt-get update && apt-get install -y build-essential
RUN mkdir -p /var/www/html && \
    pip install uwsgi
COPY requirements.txt /var/www/html
WORKDIR /var/www/html
RUN pip3 install -r requirements.txt
COPY . /var/www/html
EXPOSE 8000
CMD ["uwsgi", "--chdir=/var/www/html", "--py-autoreload=1", "--module=django_tutorial.wsgi", "--http", ":8000", "--processes=1", "--uid=1000", "--gid=2000", "--max-requests=5000", "--master"]