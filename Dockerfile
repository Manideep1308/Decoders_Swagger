FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY decode_swagger.py .


EXPOSE 1021

CMD ["python", "decode_swagger.py"]