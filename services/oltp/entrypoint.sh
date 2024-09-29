#!/bin/sh
echo "Waiting for kafka..."

    while ! nc -z $KAFKA_HOST $KAFKA_PORT; do
      sleep 1
    done

    echo "Kafka started"

exec "$@"