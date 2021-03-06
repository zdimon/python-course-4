# Встроенные функции Python.

Это функции, которые не требуют импорта и идут из коробки.

Рассмотрим некоторые из них.
 
###map(function, iterable, ...)

Применяет функцию, которая передается в качестве первого параметра, к каждому элементу
списка, переданного в качестве второго параметра.

Возвращает результат в виде списка.

### Например.

    items = [1, 2, 3]
    print items

    def mf(x):
        return x**2

    result = map(mf,items)
    print result


### Использование лямбда функции.

**лямбда функция** - это функция без названия (анонимная).

### Формат определения

    lambda <переменная, передаваемая параметром ф-ции> : <операция, возвращаемая функцией>

Применяется для более короткой записи для улучшения читабельности кода т.к. при такой конструкции
нет необходимости определять функцию под каким то именем потому что она используется только в одном месте.

Но это не значит что мы не можем присвоить лямбда функцию переменной.

    items = [1, 2, 3]
    lm = lambda x: x**2
    l = map(lm, items)
    print l

    l = map(lambda x: x**2, items)
    print l


### Вывод

    [1, 2, 3]
    [1, 4, 9]


    words = ['It', 'is', 'raining', 'cats', 'and', 'dogs'] 
    lengths = map(lambda word: len(word), words)

    >> [2, 2, 7, 4, 3, 4]



###filter(function, iterable)

Похоже на предыдущую тем, что тоже принимает два аргумента и применяет функцию
к каждому элементу переданного списка, но filter формирует и возвращает список 
из тех элементов списка для которых функция возвращает True.

Для этого каждый элемент списка будет передан в функцию-обработчик в качестве параметра.



    lst = [1,2,3,4,5,6,7,8,9]
    def myf(x):
        if x%2 == 0:
            return True
        else:
            return False

    res = filter(myf,lst)
    print res

    >> [2, 4, 6, 8]



###enumerate(sequence, start=0)

Применяется для коллекций (строки, списки, словари и или любым другим объектом, поддерживающим итерацию и

создает объект, который генерирует кортежи, состоящие из двух элементов - индекса элемента и самого элемента.


    >>> a = [10, 20, 30, 40]
    >>> for i in enumerate(a):
    ...     print(i)
    ... 
    (0, 10)
    (1, 20)
    (2, 30)
    (3, 40)

Пример аналога работы без применения enumerate:

    lst = ['one','two','three']

    for i in range(len(lst)):
        print '%s-%s' % (i,lst[i])


    for i,x in enumerate(lst):
        print '%s-%s' % (i,x)
        
В случае словарей нумеруются ключи:

    >>> c = {1: 'a', 2: 'b', 3: 'c'}
    >>> for i in enumerate(c):
    ...     print(i)
    ... 
    (0, 1)
    (1, 2)
    (2, 3)   
    
Функция enumerate() используется для упрощения прохода по коллекциям в цикле, 
когда кроме самих элементов требуется их индекс.

###Функция list([iterable])

Создает список из того, что ей передано.

Если передан словарь то создается список из его ключей.

    print list() >> []
    print list('abc') >> ['a','b','c']
    print list((5,6,7)) >> [5,6,7]
    print list({'1':'hi', '2': 'bye'}) >> ['1', '2']

###Функция dict()

С помощью этой функции мы можем создать словарь из переданного значения
в качестве которого передается список кортежей, которые будут преобразованы
в ключ и значение словаря.


    pairs = [("cat", "meow"), ("dog", "bark"), ("bird", "chirp")]

    # Преобразование
    lookup = dict(pairs)



###Output

    {'bird': 'chirp', 'dog': 'bark', 'cat': 'meow'}



### Функция tuple([iterable])


Возвращает кортеж с элементами в таком же порядке, каким он был в переданном списке.

    tuple([1, 2, 3]) returns (1, 2, 3)

 



