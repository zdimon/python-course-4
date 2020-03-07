## Создание проекта.

## Создание папки проекта.

    mkdir exel
    cd exel

## Виртуальное окружение

**установка в систему нужных команд (установщик python pip и virtualenv)**

    sudo apt-get install python3-pip virtualenv

**установка виртуального окружения в проект**

    virtualenv -p python3 venv
    
- создается папка venv где будут requirements-ы, которую обычно игнорят в git.

## Активация виртуального окружения

    . ./venv/bin/activate

**появляется приставка (venv) в начале коммандной строки что значит что окружение активировано и 
мы можем устанавливать в него необходимы пакеты**

## Установка Django 

    pip install django
    
## Создание нового проекта

    django-admin startproject prj
    
## Создание приложения

    cd djangoprj
    ./manage.py startapp main

## Прописываем название нового приложения в настройках djangoprj/settings.py



    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'main'
    ]

## Запуск сервера разработки.

    ./manage.py runserver 9898
    
    
    
## Установка системных библиотек для работы с MySQL.

    sudo apt-get install python3-dev libmysqlclient-dev build-essential    
    
## Установка клиента MySQL.

    pip install mysqlclient
    
## Прописываем коннект r базе в settings.py.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': './prj/my.cnf',
            },
        }
    }   
        

## Файл prj/my.cnf   

    [client]
    database = locotrade_new
    user = root
    password = password
    default-character-set = utf8
   
   
## Создаем файл с классами моделей существующей БД.   
   
    ./manage.py inspectdb > out-models.py
    
## Скопируем из файла out-models.py класс с пользователями в файл main/models.py.

    class Users(models.Model):
        email = models.CharField(unique=True, max_length=191)
        password = models.CharField(max_length=191)
        active = models.IntegerField()
        remember_token = models.CharField(max_length=100, blank=True, null=True)
        created_at = models.DateTimeField(blank=True, null=True)
        updated_at = models.DateTimeField(blank=True, null=True)
        deleted_at = models.DateTimeField(blank=True, null=True)
        first_name = models.CharField(max_length=191, blank=True, null=True)
        last_name = models.CharField(max_length=191, blank=True, null=True)
        phone = models.CharField(max_length=191, blank=True, null=True)

        class Meta:
            managed = False
            db_table = 'users'
        
        
## Создадим новую команду.

    cd main
    mkdir  management
    touch management/__init__.py
    mkdir management/command
    touch management/command/__init__.py
    touch management/command/load_users.py
    
Файл load_users.py.
    
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load Users')   
    
## Запуск команды.

    ./manage.py load_users

## Проходим циклом по таблице с пользователями.    
    
    print('Load Users')
    for user in Users.objects.all():
        print(user.email)    
    
## Установка библиотеки для работы с xls файлами НА ЗАПИСЬ!.

[Документация](https://pypi.org/project/xlwt/)

    pip install xlwt
    

## Создание файла exel.

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0, 'Hello world!!!')
    ws.write(0, 1, 12345)
    wb.save('example.xls')')












