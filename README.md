## Первый запуск
``` 
make launch_ch (Запуск контейнеров ClickHouse)
make storages_ch (Создание БД и таблиц в ClickHouse)
make launch_etl (Запуск всех сервисов)
``` 

## Запуск сервисов при существующих БД и таблицах
``` 
make launch_etl
``` 

## Выбор OLAP хранилища

#### Диаграмма результатов

![Сравнительные тесты ClickHouse vs Vertica](benchmark/olap/media/diagram.png?raw=true "Сравнительные тесты ClickHouse vs Vertica")

``` 
Строк для записи – 5 000 000
Запросов на чтение – 5 000
Размер партии – 500
Результат – время в секундах
``` 
