FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --upgrade pip -r requirements.txt
RUN apt-get update && apt-get install -y netcat

COPY . /app
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
EXPOSE 5000