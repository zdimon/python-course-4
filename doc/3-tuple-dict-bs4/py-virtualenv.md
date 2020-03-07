## Установщик pip. Виртуальное окружение.

При разработке программ на Python часто возникает необходимость
в установке сторонних библиотек (пакетов) , не входящих в поставку Python.

После установки появляется возможность их импорта и использования.

Установить пакет python можно вручную, распаковав архив в нужное место.

Первым делом Python пытается найти импортируемую библиотеку в текущем каталоге.

Это можно проверить, создав файл библиотеки mylib.py.

    print('Importing mylib')
    
И в другом файле попытаться его импортировать.

    import mylib
    
Вывод.
    
    shell>python imp.py 
    Importing mymodule
    shell>
    
Если файл положить в каталог lib например, то импорт будет следующим:

    import lib.mylib
    
При этом необходимо не забыть создать в каталоге специальный файл __init__.py который обозначит этот 
каталог как пакет и сделает возможным импорт из него.

Установщик pip облегчает задачу установки пакетов.

Он оперирует репозиторием пакетов на сайте https://pypi.org и тянет их от туда.

Установить его в систему можно командой.

    apt install python-pip
    
После чего использование будет в таком формате.

    pip install package_name1 package_name2
    
Мы можем создать список всех необходимых библиотек в файле requirements.txt (например) перечислив их в столбик.

    packege_name1
    package_name2
    
И потом воспользоваться ключем -r для передачи файла-списка в установщик pip.

    pip install -r requirements.txt    
    

Где еще Python ищет библиотеки при импорте?

Посмотреть все пути по которым проходит поиск можно в переменной PYTHONPATH, используя модуль sys.

Этот модуль взаимодействует напрямую с интерпретатором Python.

    import sys
    print(sys.path)

Можно запустить одной командой прямо из bash консоли.

    python -c "import sys; print('\n'.join(sys.path))"
    
Вывод

    /usr/lib/python2.7
    /usr/lib/python2.7/plat-x86_64-linux-gnu
    /usr/lib/python2.7/lib-tk
    /usr/lib/python2.7/lib-old
    /usr/lib/python2.7/lib-dynload
    /home/zdimon/.local/lib/python2.7/site-packages
    /usr/local/lib/python2.7/dist-packages
    /usr/lib/python2.7/dist-packages
    /usr/lib/python2.7/dist-packages/PILcompat
    /usr/lib/python2.7/dist-packages/gtk-2.0
    /usr/lib/python2.7/dist-packages/ubuntu-sso-client
    /usr/lib/python2.7/dist-packages/wx-3.0-gtk2
    
Как видим почти все пути являются системными и прав на запись в них имеет только привелигерованные пользователи.

Поэтому при попытке просто установить какой либо пакет запустив к примеру  

    pip install markdown 
    
Вы получите ошибку прав доступа так как текущий пользователь не может писать в /usr/local/lib/python2.7/dist-packages.

    ERROR: Could not install packages due to an EnvironmentError: 
    [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/markdown    
        
Выход из этой ситуации - это изменить переменную окружения интерпретатора sys.path, указав в нем путь нашего проекта вместо системных путей.

Это обеспечивает такая программа как virtualenv.

## Установка

    apt install virtualenv
    
    
Создание виртуального окружения.

    virtualenv venv # python 2 
    
    virtualenv -p python3 venv  # python 3
    
При этом venv - произвольное имя папки, которая создается в текущей директории.

Обычно ее создают рядом с директорией проекта, или внутри нее.

После создания этой директории необходимо запустить bash скрипт activate из каталога venv/bin.

Именно он и будет изменять пути в sys.path к нашим зависимостям.

После активации мы увидим префикс (venv) в командной строке консоли, означающий то, что теперь при использовании pip
установщика он будет ставить пакеты не в системные каталоги а внутрь нашего виртуального окружения.

Это каталог venv/lib/python3.5/site-packages/. 



   
    
    
       
    
    
    

       
    
    
    
    

