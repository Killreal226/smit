# Тестовое задание

## Способ развертывания:

1. Клонируйте себе репозиторий с GitHub.
2. Установите, если не установлен Docker.
3. В корне проекта создайте папку `config` и в ней файл `conf.env`:

    Пример содержимого `conf.env`:
    ```bash
    DB_HOST = "postgres"
    DB_PORT = 5432
    DB_NAME = "smit"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "postgres"
    DB_TABLE_NAME = "tariff"

    POSTGRES_DB = "smit"
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "postgres"

    KAFKA_BROKER_URL = "kafka:9092"
    KAFKA_TOPIC = "smit"
    ```

4. Поднимите контейнер с Postgres командой:
    ```bash
    docker compose -f docker-compose-postgres.yaml up -d --build --force-recreate
    ```

5. Поднимите контейнеры с Kafka и самим приложением командой:
    ```bash
    docker compose -f docker-compose-core.yaml up -d --build --force-recreate
    ```

6. Перейдите на `localhost:9000/docs`, где будут различные точки для тестирования.
