FROM python:3.11-slim

WORKDIR /task

COPY . .

CMD ["python", "logger.py"]



