# FROM alpine:latest
FROM python:3.12-slim

#RUN apk add --no-cache python3 py3-pip

RUN pip install flask redis

WORKDIR /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]