class Settings:
    user_num: int = 100              # Количество пользователей кинотеатра.
    films_num: int = 100             # Количество фильмов в базе кинотеатра.
    films_max_length: int = 150*60   # Максимальная длина фильма в секундах.
    ch_batch_size: int = 500         # Количество одновременно загружаемых в базу ClickHouse строк.
    vertica_batch_size: int = 500    # Количество одновременно загружаемых в базу Vertica строк.
    data_volume: int = 10 ** 6 * 5   # Общее количество строк в базе.
    requests_num: int = 10 ** 3 * 5  # Количество запросов к базе на получение информации.


settings = Settings()
