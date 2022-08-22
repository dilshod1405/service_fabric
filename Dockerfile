FROM python:3.10

WORKDIR /code

COPY requirements.txt /code/

COPY entrypoint.sh /code/

RUN chmod +x entrypoint.sh

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

ENTRYPOINT ['./entrypoint.sh']