# Работа со строками.

[Ссылка на документацию](https://docs.python.org/2/library/string.html)
 
## Доступ по ключу, срез.

    ms = 'My string'
    print(ms[0])
    print(ms[0:3])
    
Пробуем поменять символ.

    ms[1] = 'e'
    
    TypeError: 'str' object does not support item assignment
    
Строка это неизменяемый тип, поэтому изменять нужно функциями (методами), которые возвращают новый, 
измененный экземпляр строки.

Например.

    ns = ms.replace('M','W')
    >> Yy string
    
    
## Форматирование строк.

[Типы операций со строками](https://docs.python.org/3.4/library/string.html)

Форматирование можно сделать с помощью оператора %, либо с помощью метода format.

### Знак **%**

    s = 'hello %s' % 'dima'
    d = 'hello %s your number is %d' % ('dima', '4')
    
### Оператор format.

    '{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
    '{0}, {1}, {2}'.format('a', 'b', 'c')
    '{2}, {1}, {0}'.format('a', 'b', 'c')
    
    
Любая строка это объект питон со всеми атрибутами и методами поэтому 
вызывать методы можно стразу позле определения строки после кавычек.    
    
### Проверка типов.
    
    str = 'x = {x_coord}, y = {y_coord:d}'.format(x_coord=23,y_coord=56)
    
Форматирование числа.

    {:,}'.format(1234567890)
    
Приведение к одному формату (с нулями впереди).


    month = '{:02d}'.format(3)

Отсечение чисел после запятой.

    print('{:.2f}'.format(222.3333))
    
### Форматирование даты.

    import datetime
    n = datetime.datetime.now()
    '{:%Y-%m-%d %H:%M:%S}'.format(n)


### Разбиение 

    s = 'one,two,three'.split(',')

### Слияние

    '-'.join(s)    
    
### Поиск

    string.find(s)
    string.rfind(s)    
    
Возвращает число (позиция) первого вхождения или -1 при неудаче.

    string.index(s)

Работает так же как find но вызывает исключение при ненахождении.


### Поиск по регулярным выражениям.

    import re
    str = 'My name is dima. My name is dima.'
    rez = re.search('is(.*)\.',str)
    print(rez.group(1))
    
 
[Документация по регулярным выражениям](https://docs.python.org/3/library/re.html) 

## Изменение регистра 

    str.capitalize(); str.lower(); str.upper()

## Убираем пробелы вначале и в конце.

    '   spacious   '.strip()











       
