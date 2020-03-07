##Словари.

Перечисляемые структуры данных, определяемые в виде пар ключ - значение внутри фигурных скобок 
через двоеточие и разделенных запятой.

## Доступ к значениям элементов словаря по ключу.

    #!/usr/bin/python

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print dict['Name']


Ключ может быть числом.

    dict = {1: 'one', 2: 'two'}
    print dict[1]
    print dict[3]

    Traceback (most recent call last):
      File "dict_ex.py", line 3, in <module>
        print dict[3]
    KeyError: 3

Безопасное извлечение.

    print dict.get(3,'no')

### Изменение словаря

    
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    dict['Age'] = 8; # update existing entry
    dict['School'] = "DPS School"; # Add new entry


### Удаление элементов из словаря.

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    del dict['Name']; # remove entry with key 'Name'
    dict.clear();     # remove all entries in dict
    del dict ;        # delete entire dictionary

### Ключ должен быть неизменяемым объектом.


    dict = {['Name']: 'Zara', 'Age': 7}


    Traceback (most recent call last):
       File "test.py", line 3, in <module>
          dict = {['Name']: 'Zara', 'Age': 7};
    TypeError: list objects are unhashable




### Встроенные функции работы со словарем.


Создание словаря.

        
    md = dict(name='Vova', age=23)

    print(md)


### Длинна словаря

    len(dict)

### Строковое представление.

    str(dict)
    type(variable)


	
### Создание словаря из 2 списков функцией zip.

    d1 = ['one', 'two', 'three']
    d2 = [1, 2, 3]
    d3 = dict(zip(d1,d2))
    print(d3 

    >> {'three': 3, 'two': 2, 'one': 1}

### Встроенные методы словарей.

    dict.clear() # очистить
    dict.copy() # склонировать (сделать копию)


    

    dict.fromkeys(seq[, value])

Create a new dictionary with keys from seq and values set to value.

    seq = ('name', 'age', 'sex')
    val = (10,20,30)
    dict = dict.fromkeys(seq,val)
    print dict
    >> {'age': (10, 20, 30), 'name': (10, 20, 30), 'sex': (10, 20, 30)}

    dict.get(key, default=None)


Проверка на существование ключа.
	
    dict.has_key(key)  # only for Python 2!



### Получение всех ключей словаря.
	
    print(dict.keys())
    
    >> dict_items([('two', [1, 2, 3]), ('one', [1, 2, 3]), ('three', [1, 2, 3])]) # python 3
    >> [('three', [1, 2, 3]), ('two', [1, 2, 3]), ('one', [1, 2, 3])] # python 2

### Получение всех значений словаря.

    print(dict.values())
    >> dict_values([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) # python 3
    >> [[1, 2, 3], [1, 2, 3], [1, 2, 3]] # python 2


### Получение всех ключей-значений словаря.
	
    print(dict.items())
    
    >> dict_items([('two', [1, 2, 3]), ('one', [1, 2, 3]), ('three', [1, 2, 3])]) # python 3
    >> [('three', [1, 2, 3]), ('two', [1, 2, 3]), ('one', [1, 2, 3])] # python 2
    

## Обход словаря в цикле.


    for key, value in d.iteritems(): # For Python 2.x

    for key, value in d.items(): $ for Python 3.x
    
    
### Альтернативный способ обхода по ключам **dict.keys()**.

    for key in d3.keys():
        print(d3[key])
        

### Массовое обновление словаря словарем.


    dict.update(dict2)

Функция НЕ возвращает а изменяет словарь.

### Преобразование словаря в строку json.


    import json
    
    json.dumps({"one": 1, "two": '2'})
    
Запишем в файл.
    
    # write into file
    f = open('tst.txt','w+')
    f.write(s1)
    f.close()
    
Для записи строки ее нужно преобразовывать из объекта словаря в строку функцией dumps.
    
Считаем из файла.

    # read from file
    f = open('tst.txt','r')
    st = f.read()
    f.close()
    st_dict = json.loads(st)
    print(st_dict['two'])    
        
Для работы со словарем его необходимо преобразовывать из строки в объект ф-цией loads.        
 
        
        
    
    

