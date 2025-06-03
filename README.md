Управление денежными потоками
Это веб-приложение на Django для управления денежными потоками, позволяющее пользователям добавлять, редактировать, удалять и фильтровать финансовые записи. Приложение поддерживает русский интерфейс (ru-ru) и предоставляет функционал для управления категориями, подкатегориями, типами и статусами.
Основные возможности

Добавление и редактирование записей: Создание и изменение финансовых записей с указанием даты, суммы, типа, категории, подкатегории, статуса и комментария.
Фильтрация записей: По диапазону дат, статусу, типу, категории и подкатегории с динамическими выпадающими списками.
Удаление записей: Удаление записей с подтверждением.
Управление справочниками: Добавление и удаление статусов, типов, категорий и подкатегорий через интерфейс.
REST API: Используется для динамического обновления выпадающих списков категорий и подкатегорий.
Русская локализация: Полный перевод интерфейса на русский язык.
Адаптивный дизайн: Интерфейс построен с использованием Bootstrap 5 для удобства на десктопах и мобильных устройствах.

Требования

Python: 3.8+ (рекомендуется 3.11, так как Django 4.2.7 не поддерживает Python 3.7)
База данных: SQLite (встроена в Python, не требует установки)
Операционная система: Windows, macOS, Linux
Git: Для клонирования репозитория (опционально)
pip: Для установки зависимостей
virtualenv (рекомендуется): Для изоляции окружения
Интернет-соединение: Для загрузки Bootstrap 5 через CDN (если не используете локальные файлы)

Установка и настройка
1. Клонирование репозитория
Склонируйте репозиторий или распакуйте проект:
git clone <URL_репозитория>
cd cashflow_project

Замените <URL_репозитория> на URL вашего репозитория. Если проект уже скачан, перейдите в папку:
cd путь/к/cashflow_project

2. Создание виртуального окружения
Создайте и активируйте виртуальное окружение:
python -m venv venv


Windows:venv\Scripts\activate


macOS/Linux:source venv/bin/activate



3. Установка зависимостей
Установите Python-зависимости из requirements.txt:
pip install -r requirements.txt

Содержимое requirements.txt:
Django==4.2.7
python-decouple==3.8
djangorestframework==3.14.0


Django==4.2.7: Основной фреймворк.
python-decouple==3.8: Для работы с переменными окружения (например, SECRET_KEY).
djangorestframework==3.14.0: Для REST API (динамические выпадающие списки).

Front-end зависимости:

Bootstrap 5.3.3 включается через CDN в base.html:<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

Если вы предпочитаете локальные файлы, скачайте их с getbootstrap.com и поместите в static/bootstrap/, обновив base.html.

4. Настройка базы данных (SQLite)
SQLite встроен в Python и не требует отдельной установки.

Проверьте настройки в settings.py:В cashflow_project/settings.py убедитесь, что:
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Файл db.sqlite3 создастся автоматически.

Настройте переменные окружения:Создайте файл .env в корне проекта:
echo "SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" > .env
echo "DEBUG=True" >> .env

В settings.py добавьте:
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)


Примените миграции:
python manage.py makemigrations
python manage.py migrate



5. Подготовка статических файлов и переводов

Соберите статические файлы (для custom.css и Bootstrap, если локально):
python manage.py collectstatic --noinput

Убедитесь, что в settings.py:
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


Скомпилируйте переводы (для русского интерфейса):
python manage.py compilemessages

Проверьте локализацию в settings.py:
LANGUAGE_CODE = 'ru-ru'
USE_I18N = True
USE_TZ = True
TIME_ZONE = 'UTC'  # Или 'Europe/Moscow'



6. Создание суперпользователя
Создайте учетную запись для доступа к админ-панели:
python manage.py createsuperuser

Введите имя пользователя, email и пароль.
7. Запуск веб-сервиса
Запустите сервер разработки:
python manage.py runserver


Откройте браузер: http://127.0.0.1:8000/.
Админ-панель: http://127.0.0.1:8000/admin/.

Использование

Главная страница (/): Просмотр записей с фильтрами по дате, статусу, типу, категории и подкатегории.
Добавление записи: Кнопка «Добавить запись» открывает форму.
Редактирование/удаление: Кнопки «Редактировать» и «Удалить» в таблице.
Управление справочниками: Страница /dictionary/ для добавления/удаления статусов, типов, категорий и подкатегорий.
Фильтрация: Используйте форму фильтров для выборки записей. Выпадающие списки категорий и подкатегорий обновляются динамически через REST API.

Тестирование
Добавьте тестовые данные через Django shell:
python manage.py shell

Пример:
from dds.models import Status, Type, Category, SubCategory, CashFlowRecord
status = Status.objects.create(name="Оплачено")
type_income = Type.objects.create(name="Доход")
category = Category.objects.create(name="Зарплата", type=type_income)
subcategory = SubCategory.objects.create(name="Основная", category=category)
CashFlowRecord.objects.create(
    date="2025-06-01",
    amount=50000,
    type=type_income,
    category=category,
    subcategory=subcategory,
    status=status,
    comment="Зарплата за июнь"
)

Устранение неисправностей

Ошибка: ModuleNotFoundError:Убедитесь, что все зависимости установлены:pip install -r requirements.txt


Ошибка: Стили не применяются:Проверьте, что collectstatic выполнен и Bootstrap подключен в base.html.
Ошибка: Переводы не работают:Убедитесь, что выполнена команда compilemessages.
Ошибка: NoReverseMatch или ImportError:Проверьте urls.py и views.py на наличие всех маршрутов и импортов.

Для продакшена

Установите DEBUG = False в settings.py.
Используйте WSGI-сервер (например, gunicorn):pip install gunicorn
gunicorn cashflow_project.wsgi:application --bind 0.0.0.0:8000


Настройте Nginx для статических файлов.
Рассмотрите PostgreSQL вместо SQLite для масштабируемости.

Лицензия
[Укажите лицензию, например, MIT или проприетарную]
Контакты
Для вопросов или предложений свяжитесь через [ваш email или GitHub].
