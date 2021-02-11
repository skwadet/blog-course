# Курс Django REST Framework

Будем создавать сервис микроблоггинга в REST стиле в целях обучения.

1. Сперва опишем модели и связи между ними
1. Определим нужные нам запросы к БД
1. Создадим базовую бизнес-логику
1. Напишем views
1. Доработаем бизнес-логику под все кейсы
1. Напишем тесты
1. Задеплоимся

Курс покроет весь необходимый набор для понимания работы веб-приложений.


Стек - Poetry, Django, Django REST Framework, Django Filter, PyTest, Celery, Redis, PostgreSQL, Docker

Поднять проект:
1. sudo systemctl start docker (не всегда автоматически запускается)
1. Из коревой папки проекта: sudo docker-compose up -d postgres

Credits:
1. etobaza (Artyom Todosiev) - Main Developer
1. skwadet (Evgeniy Bazarov) - Project Manager
1. alex-npmn (Alexey Nepomnyashchikh) - Code Reviewer

Must read:
- Django
1. https://docs.djangoproject.com/en/3.1/topics/db/models/
1. https://docs.djangoproject.com/en/3.1/topics/db/queries/
1. https://docs.djangoproject.com/en/3.1/ref/request-response/

- Django REST Framework
1. https://www.django-rest-framework.org/
1. https://webdevblog.ru/sozdanie-django-api-ispolzuya-django-rest-framework-apiview/

- SQL
1. https://www.w3schools.com/sql/

- Python lib
1. https://docs.python.org/3/library/index.html
1. https://docs.python.org/3/tutorial/index.html

- Git
1. https://www.atlassian.com/ru/git/tutorials/comparing-workflows/gitflow-workflow
1. https://git-scm.com/book/ru/v2
