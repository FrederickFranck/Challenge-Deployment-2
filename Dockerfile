FROM python:3.9-slim-buster
RUN apt-get update && apt -yy install \
    wget \
    curl \
    gcc \
    && wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup \
    && echo "d4e4635eeb79b0e96483bd70703209c63da55a236eadd7397f769ee434d92ca8  mariadb_repo_setup" \
    | sha256sum -c - \
    && chmod +x mariadb_repo_setup \
    && ./mariadb_repo_setup \
    --mariadb-server-version="mariadb-10.6" \
    && apt-get -yy install libmariadb3 libmariadb-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get -yy remove --auto-remove curl \
    && apt-get -yy remove --auto-remove wget 
COPY ./project/requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt 
COPY ./project/uninstall.txt /
RUN pip uninstall -y -r uninstall.txt
RUN apt-get -yy remove --auto-remove gcc 
COPY ./project /project
WORKDIR /project
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]