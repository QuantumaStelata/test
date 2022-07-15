## Установите виртуальное окружение
        python3 -m venv venv

## Активируйте виртуальное окружение
        .\venv\Script\activate

## Установите зависимости
        pip3 install -r requirements.txt

## Проведите миграцию базы данных
        python3 manage.py migrate

## Запишите тестовые данные в базу данных, либо используйте свои данные
        python3 manage.py loaddata terms
        python3 manage.py loaddata brands
        python3 manage.py loaddata styles