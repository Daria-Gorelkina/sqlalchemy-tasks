# Создание и настройка движка базы данных с использованием SQLAlchemy

В этом упражнении вам предстоит создать движок базы данных для подключения к PostgreSQL с использованием SQLAlchemy. 

## src/solution.py

Необходимо создать функцию `create_db_engine()`, которая будет создавать и возвращать объект движка базы данных для подключения к PostgreSQL. Функция должна принимать следующие параметры:

- `db_url`: строка подключения к базе данных PostgreSQL;
- `echo`: логический параметр, который включает или отключает вывод SQL-запросов в консоль (по умолчанию `False`);
- `pool_size`: целое число, определяющее размер пула соединений (по умолчанию `5`);
- `max_overflow`: целое число, определяющее максимальное количество соединений сверх размера пула (по умолчанию `10`).

Функция должна использовать `create_engine()` из SQLAlchemy для создания движка с указанными параметрами.

## .env

Добавьте в файл .*env* переменную `DATABASE_URL` с URL базы данных PostgreSQL.