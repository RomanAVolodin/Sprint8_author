from http import HTTPStatus

from api.messages import message
from core.config import settings
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from kafka import KafkaProducer
from schemas.progress import FilmProgress

film_progress_bp = Blueprint('film-progress', __name__, url_prefix='/api/v1/film-progress')
producer = KafkaProducer(bootstrap_servers=[f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}'])


@film_progress_bp.route('/', methods=['POST'])
@jwt_required()
@validate()
def film_progress(body: FilmProgress):
    value = str.encode(body.json())
    key = str.encode(f'{body.user_id}+{body.film_id}')
    producer.send(topic=f'{settings.VIEWS_TOPIC}', value=value, key=key)
    response = jsonify(message=message('send_kafka', body.user_id))
    response.status_code = HTTPStatus.CREATED
    return response
