import time

from src.components.extractor.extractor import KafkaExtractor
from src.components.loader.loader import ClickHouseLoader
from src.components.transformer.transformer import Transformer
from src.core.settings import etl_settings

if __name__ == '__main1__':
    extractor = KafkaExtractor()
    transformer = Transformer()
    loader = ClickHouseLoader()

    records = extractor.consume()

    while True:
        try:
            data_dict = transformer.transform(next(records))
        except StopIteration:
            time.sleep(etl_settings.etl_manager_timeout)
        else:
            for database, table in data_dict.items():
                for table_name, table_data in table.items():
                    loader.add_data(database, table_name, table_data.fields, table_data.data)
                    extractor.commit()
