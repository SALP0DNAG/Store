## Установите зависимости
pip install -r requirements.txt
## Создайте миграции
python manage.py makemigrations
python manage.py migrate
## Запустите сервер
python manage.py runserver