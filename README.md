## Установите виртуальное окружение
        python3 -m venv venv

## Активируйте виртуальное окружение
        .\venv\Script\activate

## Установите зависимости
        pip3 install -r requirements.txt

## Проведите миграцию базы данных
        python manage.py migrate

## Запишите тестовые данные в базу данных, либо используйте свои данные
        python manage.py loaddata terms
        python manage.py loaddata brands
        python manage.py loaddata styles