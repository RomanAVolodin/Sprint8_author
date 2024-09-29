from abc import ABC, abstractmethod


class BaseLoader(ABC):
    """ Базовый класс загрузки данных в OLAP-хранилище """

    @abstractmethod
    def add_data(self, db: str, table: str, fields: str, data: list) -> None:
        """ Вставка данных, поступающих из OLTP хранилища """
