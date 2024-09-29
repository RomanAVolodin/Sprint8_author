from api.v1.films import film_progress_bp
from core.config import settings
from extensions import jwt
from flask import Flask

app = Flask(__name__)
app.register_blueprint(film_progress_bp)
app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY


jwt.init_app(app)


def main():
    app.run(host=settings.APP_HOST, debug=settings.DEBUG)


if __name__ == '__main__':
    main()
