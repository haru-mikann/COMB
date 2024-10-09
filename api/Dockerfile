FROM python:3.12-slim

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

CMD ["uvicorn","index:app","--reload"]

