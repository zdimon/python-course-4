# Работа со списками.

Сравнение списка и словаря.

![python requests]({path-to-subject}/images/1.png)


[Ссылка на документацию](https://docs.python.org/2/library/string.html)

## Определение списков.

**Списки** - перечисляемые структуры разных элементов, заключенные в [] и разделенные запятой. 

В основном списки используются в циклах.

## Создание списков

    list1 = ['physics', 'chemistry', 1997, 2000];
    list2 = [1, 2, 3, 4, 5];
    list3 = ["a", "b", "c", "d"]
    
Создание с помощью генераторов списка.


    [выражение for переменная in последовательность условие]   
    
    lst = [i for i in range(30) if i % 3 == 0]


    [i for i in range(30) if i % 3 == 0] 


### Доступ к элементам списка, срезы.

    print(list1[0])
    print(list2[1:5])
    print(1:)
    
Срез с шагом.

    s = [1,2,3,4,5,6,7,8]
    d = s[1:7:2]
        
    
Вставка списка вместо среза.

    A = [1, 2, 3, 4, 5]
    A[2:4] = [7, 8, 9]    
    

### Основные методы работы со списками.

### Изменение списка.

Присвоением.

    list = ['physics', 'chemistry', 1997, 2000];
    print list[2] 
    list[2] = 2001;
    print list[2]
    
Добавление элементов.

    lst.append(element)

Удаление элементов.

    del list1[2];

### Получение информации о списке

    len(list) # общее количество элементов

	
    max(list) # максимальный элемент

	
    min(list) # минимальный элемент
       
    
Сложение.   
    
    [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	
    
Умножение.
    
    ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	
    
Проверка на существование элемента.    
    
    3 in [1, 2, 3]	
    
Итерация по списку.

    for x in [1, 2, 3]: print x
    
### Встроенные функции для списков.

Сравнение списков

    cmp(list1, list2)

	

Создание списка из кортежа.
	
    list(seq)


### Методы списков:


    list.append(obj) # добавление нового элемента в конец списка


    list.count(obj) # возвращает количество повторений элемента в списке


    list.extend(seq) # добавляет новый список в конец (расширяет)


    lst = [1,2,3]
    lst.extend([4,5,6])
    print lst
    >> [1, 2, 3, 4, 5, 6]

Нахождение индекса элемента.

    list.index(obj) 


    [1, 2, 3, 4, 5, 6]
    >>> print lst.index(2)
    1
    >>> print lst.index(4)
    3
    >>> print lst.index(44)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 44 is not in list


    list.insert(index, obj) # вставляет элемент в нужную позицию внутрь списка


    list.pop() # возвращает последний объект удаляя его из списка


    list.remove(obj) # просто удаляет объект из списка


    list.reverse() # переворачивает порядок элементов

### Преобразование списка в строку с разделителем.

    'разделитель'.join(list)

### Преобразование строки в список по разделителю.

    'разделитель'.join(list)


## Сортировка списков.

    list.sort([func]) 


Сортирует список применяя функцию к соседним элементам.

Если функция возвращает 1, то меняет элементы местами и идет сначала.

    lst = [2,4,7,3,9]    

    def compare(it1,it2):
        if it1>it2:
            return 1
        else:
            return -1

    lst.sort(compare)
    print lst


Compare functions specifies a custom comparison function of two arguments (list items) which should return a negative, zero or positive number.

    [('c', 4), ('b', 2), ('a', 3)] => [('c', 4), ('a', 3), ('b', 2)]

    lst = [('c', 4), ('b', 2), ('a', 3)] 

    def letter_cmp(a, b):
        if a[1] > b[1]:
            return -1
        elif a[1] == b[1]:
            if a[0] > b[0]:
                return 1
            else:
                return -1
        else:
            return 1

    lst.sort(letter_cmp)
    print lst
    
    


    


