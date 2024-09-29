import ast

import backoff
from src.components.transformer.base import BaseTransformer
from src.core.settings import backoff_config
from src.maps.maps import UserHistoryMap
from src.models.models import UserHistory
from src.utils.logger import etl_logger


class Transformer(BaseTransformer):

    def __init__(self):
        self.data_dict = {}
        self.database = UserHistoryMap.database
        self.table = UserHistoryMap.table
        self.fields = UserHistoryMap.fields
        self.model = UserHistory

    @backoff.on_exception(**backoff_config, logger=etl_logger)
    def transform(self, records: dict) -> dict:
        self.data_dict = {}
        for partition, consumer_records in records.items():
            for record in consumer_records:
                match record.topic:
                    case 'views':
                        self.database = UserHistoryMap.database
                        self.table = UserHistoryMap.table
                        self.fields = UserHistoryMap.fields
                        self.model = UserHistory
                self.add_data_to_dict(data=self.model(**ast.literal_eval(record.value.decode())).dict())

        return self.data_dict

    def add_data_to_dict(self, data: dict) -> None:
        self.data_dict.setdefault(self.database, {})

        if self.table not in self.data_dict[self.database]:
            self.data_dict[self.database][self.table] = {'fields': self.fields, 'data': []}

        self.data_dict[self.database][self.table]['data'].append(data)
