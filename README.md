# Дошка оголошень (Notice Board)

Це простий сервіс для публікації та перегляду оголошень на Django з підтримкою PostgreSQL.

## Можливості
- Публікація оголошень з категоріями, ціною, описом
- Фільтрація та сортування за категорією, ціною, датою
- Пошук по заголовку оголошення
- Коментарі до оголошень
- Адмін-панель для керування всіма моделями
- Сторінка статистики для адміністратора (опціонально)

## Встановлення
1. Клонуйте репозиторій та перейдіть у папку проекту
2. Створіть та активуйте віртуальне середовище:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Встановіть залежності:
   ```
   pip install django psycopg2-binary
   ```
4. Встановіть та запустіть PostgreSQL (наприклад, через Homebrew):
   ```
   brew install postgresql
   brew services start postgresql
   ```
5. Створіть базу даних і користувача у PostgreSQL:
   ```
   psql
   CREATE DATABASE notice_board_db;
   CREATE USER your_pg_user WITH PASSWORD 'your_pg_password';
   GRANT ALL PRIVILEGES ON DATABASE notice_board_db TO your_pg_user;
   \q
   ```
6. Вкажіть ці дані у `notice_board/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'notice_board_db',
           'USER': 'your_pg_user',
           'PASSWORD': 'your_pg_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
7. Застосуйте міграції:
   ```
   python manage.py migrate
   ```
8. Створіть суперкористувача для адмінки:
   ```
   python manage.py createsuperuser
   ```
9. Запустіть сервер:
   ```
   python manage.py runserver
   ```

## Використання
- Головна сторінка: http://127.0.0.1:8000/
- Адмін-панель: http://127.0.0.1:8000/admin/

## Додатково
- Зупинити сервер PostgreSQL: `brew services stop postgresql`
- Зупинити сервер Django: Ctrl+C у терміналі

---

**Автор:** novytskyibo
