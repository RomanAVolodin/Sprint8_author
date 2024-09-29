from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_HOST: str = 'localhost'
    DEBUG: bool = False
    KAFKA_HOST: str = 'localhost'
    KAFKA_PORT: int = 9093
    VIEWS_TOPIC: str = 'secret'
    JWT_SECRET_KEY: str = 'top_secret'
    TEST_API_URL: str = "http://kafka-test:9093/api/v1/"


settings = Settings()
