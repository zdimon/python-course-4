# Библиотека os. Работа с файловой системой.

[Ссылка на официальную документацию](https://pythonworld.ru/moduli/modul-os.html)
    
    import os
    print('OS module!')
    print(__file__)
    print(os.path.realpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))    
    
    
Вывод 

    OS module!
    os-exmpl.py
    /home/zdimon/storage1/www/wm_ve/data/python-beginner/ru/2-os-string/code/os-exmpl.py
    /home/zdimon/storage1/www/wm_ve/data/python-beginner/ru/2-os-string/code
    

**os.path.realpath** - абсолютный путь с именем файла
**os.path.dirname** - абсолютный путь без имени файла

## Текущая рабочая директория.

    path = os.getcwd()

## Создание и удаление директорий.

    newdir = 'new'
    os.mkdir(newdir)
    
Если нужно создать сразу структуру директорий.

    path = "year/month/week/day"
    os.makedirs(path)
    
Удаление одной директории.

    os.rmdir(path)
    
Если нужно удалить непустую директорию то можно использовать модуль **shutil**.

    import shutil
    shutil.rmtree('/folder_name')
    
Проверка на существование директории.

        
    if os.path.isdir('year'):
        print("Deleting year dir")
        shutil.rmtree('year')

## Работа с путями.

[Ссылка на официальную документацию](https://pythonworld.ru/moduli/modul-os.html)


**os.path.join(path1[, path2[, ...]])** - соединяет пути с учётом особенностей операционной системы.

**os.path.getsize(path)** - размер файла в байтах.

## Работа с файлами.

### Создадим в цикле несколько непустых файлов, записав в них случайное число от 100 до 200.

    import random
    
    for i in range(0,5):
        rnd = random.randint(100, 200)
        f = open(str(rnd)+'.txt','w')
        f.write(str(rnd))
        f.close()
        
При открытии файла необходимо указать режим открытия:

- **r r+** - для чтения и чтения + записи 
- **w w+** - открытие для записи w+ - создаст новый пустой если не существует
- **a a+** -  открыть для добавления в конец файла (позиционирует курсор в конец)

**random.randint(A, B)** - случайное целое число N, A ≤ N ≤ B.

[Документация по random](https://pythonworld.ru/moduli/modul-random.html)

## Открытие оператором **with**. Чтение файла.


    with open('147.txt','r') as f:
        data = f.read()
        print("Data is %s" % data)

## Получение содержимого директории.

    print("List directory")
    lst = os.listdir('.')
    print(lst)

Определение файла или директории.


    data = os.listdir('.')
    for d in data:
        if os.path.isdir(d):
            print("Directory is %s" % d)
        else:
            print("File is %s" % d)



