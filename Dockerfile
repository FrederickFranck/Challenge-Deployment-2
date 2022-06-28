FROM python:3.9-slim-buster
RUN apt-get update \
    && apt -yy install wget \
    && apt -yy install curl \
    && wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup \
    && echo "d4e4635eeb79b0e96483bd70703209c63da55a236eadd7397f769ee434d92ca8  mariadb_repo_setup" \
    | sha256sum -c - \
    && chmod +x mariadb_repo_setup \
    && ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6" \
    && apt-get -yy install libmariadb3 libmariadb-dev 
RUN pip install --upgrade pip
COPY ./project/requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt 
COPY ./project /project
WORKDIR /project
CMD ["python", "app.py"]