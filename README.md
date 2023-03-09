# CoffeeHouse_SoftwareTools

[![Build status](https://github.com/AlexanderObolonkov/CoffeeHouse_SoftwareTools/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/AlexanderObolonkov/CoffeeHouse_SoftwareTools/actions/workflows/checks.yml)

## Разработка проекта на Django

- Среда: Pycharm Professional
- Язык: Python
- Использованные библиотеки: Django и его зависимости, python-dotenv
- Фамилия разработчика: Оболонков

## Запуск

Скопируйте `.env.example` в `.env` и отредактируйте `.env` файл, заполнив в нём все переменные окружения:

```bash
cp CoffeeHouse_SoftwareTools/.env.example CoffeeHouse_SoftwareTools/.env
```

Для управления зависимостями используется [poetry](https://python-poetry.org/),
требуется Python 3.10.

Установка зависимостей и локальный деплой

```bash
poetry install
```

Запуск окружения Poetry и проекта

```bash
poetry shell
python manage.py collectstatic
python manage.py loaddata db.json  # Опционально
python manage.py runserver
```