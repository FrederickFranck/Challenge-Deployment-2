FROM python:3.9-slim-buster
COPY ./project/requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt 
COPY ./project /project
WORKDIR /project
CMD ["python", "app.py"]