## pysocial by Django

Backend cоциальной сети на Django Rest Framework.

#### Стек технологий:
* Python
* Django Rest Framework
* PostgreSQL

## Как запустить:
#### 1) Установить Docker на компьютер
#### 2) Клонировать этот репозиторий
#### 3) В корне создать файл .env.dev
    DEBUG=1
    SECRET_KEY=a20335f439df3ae1412648dac9aee19e
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DB=pysocial
    POSTGRES_USER=pysocial_user
    POSTGRES_PASSWORD=pysocial_pass
    POSTGRES_HOST=pysocial_db
    POSTGRES_PORT=5432
    DATABASE=postgres

    DEFAULT_FROM_EMAIL=your@your.com
    EMAIL_USE_TLS=True
    EMAIL_HOST=your_smtp
    EMAIL_HOST_USER=your@your.com
    EMAIL_HOST_PASSWORD=pass
    EMAIL_PORT=587
   
#### 4) Создать образ Docker
    docker-compose build
#### 5) Запустить контейнер Docker
    docker-compose up
#### 6) Перейти по адресу
    http://127.0.0.1:8000/api/v1/swagger/
