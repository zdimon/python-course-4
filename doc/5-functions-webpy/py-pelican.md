# Пеликан.

Инструмент для создания статического сайта.

Хорошо подходит для документаций, блогов и пр.

Позволяет хранить данные в текстовых файлах в формате rst или md.

Автоматически формирует статичный html, подготавливая сайт к деплою.

Предоставляет много плагинов, включая темы оформления.

#Создание и активирование окружения.

    virtualenv venv
    . ./venv/bin/activate


#Установка пакетов.

    pip install pelican markdown

##Создание проекта.

    mkdir site
    cd site
    pelican-quickstart
    
## Наполнение контентом.    
    
Создаем файл статьи в каталоге content/keyboard-review.md.

    Title: Заголовок
    Date: 2010-12-03 10:20
    Category: Review

    Following is a review of my favorite mechanical keyboard.


### Главная страница

    content/pages/home.md:

    Title: Welcome to My Site
    URL:
    save_as: index.html

    Thank you for visiting. Welcome!


Создание страницы и сборка

    pelican content

Запуск сервера

    cd output
    python -m SimpleHTTPServer
    
## Использование плагинов.    
   
### Темы   
    
git clone --recursive https://github.com/getpelican/pelican-themes ./themes    
THEME = "themes/bootstrap2"    

### PlantUML плагин

http://plantuml.sourceforge.net/

    #!/bin/bash
    java -jar /opt/plantuml/plantuml.jar ${@}
    
sudo apt-get install graphviz    

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['plantuml', 'sitemap']

Пример диаграммы.

    .. uml::

        @startsalt
        {
        {T
         + <&folder>o_ve
         ++ <&folder>o
         +++ <&folder>o
         +++ <&file>urls.py
         +++ <&file>wsgi.py
         +++ <&file>urls.py
         +++ <&file>settings.py
         ++ <&folder>blog
         +++ <&folder>migrations
         +++ <&file>views.py
         +++ <&file>tests.py
         +++ <&file>models.py
         +++ <&file>admin.py   
         + <&file>ft.py
         + <&file>db.sqlite3
         + <&file>manage.py   
        }
        }
        @endsalt








