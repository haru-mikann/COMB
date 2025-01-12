FROM python:3.12-slim

WORKDIR /bot

COPY requirements.txt requirements.txt

RUN apt update && apt install -y ffmpeg && pip install -r requirements.txt

CMD ["python","main.py"]