# Тестовое задание для компании Webtronics

## Быстрый старт

1. Склонируйте репозиторий и перейдите в папку проекта

```shell
git clone https://github.com/codenjoyer/blogpost.git
```

2. Создайте виртуальное окружение и активируйте его

```shell
python -m venv venv
source venv/bin/activate
```

3. Установите зависимости

```shell
pip install -r requirements.txt
```

4. Запустите миграции

```shell
alembic upgrade head
```

5. Запустите приложение

```shell
uvicorn main:app --reload
```

## Описание

Небольшое приложение, социальная сеть, с базовой реализацией REST API. Есть авторизация, возможность создания
публикаций и реагирования на них.

## Технологии

- Python 3.11
- FastAPI
- FastAPI-Users
- SQLite 3
- Aiosqlite
- SQLAlchemy
- Alembic