FROM python:3.10-slim

RUN mkdir sy

WORKDIR /sy

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir /logs

EXPOSE 2517

CMD ["python", "main.py"]
