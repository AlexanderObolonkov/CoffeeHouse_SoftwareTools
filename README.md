# CoffeeHouse_SoftwareTools

[![Build status](https://github.com/AlexanderObolonkov/CoffeeHouse_SoftwareTools/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/AlexanderObolonkov/CoffeeHouse_SoftwareTools/actions/workflows/checks.yml)

<img src="https://raw.githubusercontent.com/AlexanderObolonkov/CoffeeHouse_SoftwareTools/c7677626082125fc5ccaf99bb5bffded88b37b5d/mysite/static/img/logo.svg" alt="logo" width="200">

Django coffee site

## Tech stack

- [Python](https://www.python.org)
- [SQLite](https://sqlite.org/index.html)


## Dependencies
[Here](https://github.com/AlexanderObolonkov/CoffeeHouse_SoftwareTools/blob/main/pyproject.toml)

## Local Developing

To manage dependencies, use [Poetry](https://python-poetry.org/), Python 3.10 required.

1) Copy `.env.example` in `.env` and edit `.env` file, fill environment variables:
    ```bash
    cp CoffeeHouse_SoftwareTools/.env.example CoffeeHouse_SoftwareTools/.env
    ```

2) Install packages
    ```bash
    poetry install
    ```

3) Run Poetry:
    ```bash
    poetry shell
    ```

4) Run project dependencies, migrations, fill the database with the fixture data etc.:
    ```bash
    python manage.py migrate
    python manage.py loaddata <path_to_fixture_files>
    python manage.py collectstatic
    python manage.py runserver
    ```   
## Developers
- Obolonkov Alexander
  Username: AlexanderObolonkov
- Gaykin Kirill
  Username: GovardFilipsovich
- Veselov Anton
  kartofanChick22
