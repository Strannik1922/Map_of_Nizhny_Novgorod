# Map_of_Nizhny_Novgorod

## Стэк:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)

## Описание:
Map_of_Nizhny_Novgorod - веб-приложение, при открытии которого выводится карта Нижнего Нвогорода. Было добавлено пару интересных мест на карту и описание к ним в фреймах точки. Для карты была использована библиотека folium.

## Установка и запуск проекта на локальном компьютере:

#### 1. Клонируйте репозиторий:
```bash
git clone git@github.com:Strannik1922/Map_of_Nizhny_Novgorod.git
```

#### 2. Перейдите в директорию проекта:
```bash
cd Map_of_Nizhny_Novgorod/
```

#### 3. Создайте и активируйте виртуальную среду:
```bash
python -m python venv
source python/Scripts/activate
```

#### 4. Обновить pip:
```bash
python -m pip install --upgrade pip
```

#### 5. Импорт requirements.txt
```bash
pip install -r requirements.txt
```

#### 6. Не забудьте провести миграции:
```bash
python manage.py migrate
```