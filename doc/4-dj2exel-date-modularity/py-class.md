# Классы

Класс - это проект объекта.

Классы состоят из свойств и методов.

Свойства - переменные класса.

Методы - функции класса.

Простейшая форма определения класса:

    class ClassName(object):
        <statement-1>
        .
        .
        .
        <statement-N>
        
В скобках мы указываем от чего наследуется класс. 

В python 3 указание (object) не обязательно.

Имя должно быть с заглавной буквы. 

При наследовании класс-потомок получает все методы и свойства от родительского.

Пример класса.

    class User(object):
        """docstring - a simple example class"""
        name = 'Dima'
        def say_name(self):
            print('my name is %s' % name)


    user = User()
    user.name
    user.say_name()
    
 
    
В питоне все является объектами какого либо класса.

Для того, чтобы посмотреть какому классу принадлежит объект можно воспользоваться функцией type().

    >>> type('hello')
    <type 'str'>
    >>> type(2)
    <type 'int'>
    >>> type(2.)
    <type 'float'>

Для того, чтобы посмотреть структуру объекта можно воспользоваться функцией dir().

    print(dir(object))
    
    
Результат вывода структуры объекна целого числа.

    dir(3)
    
    >>> ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
        
С подчеркивания начинаются служебные (внутренние) методы, которые программисту вызывать не нужно.        
    
У классов есть особый метод, под названием __init__ (конструктор).

Этот метод вызывается всякий раз, когда вы создаете (или создаете экземпляр) объект на основе этого класса.

Метод __init__ вызывается один раз, и не может быть вызван снова внутри программы. 

В этом методе обычно проводят инициализацию свойств создаваемых объектов.


    class Animal(object):
        """docstring"""

        def __init__(self, color, size):
            """Constructor"""
            self.color = color
            self.size = size

        
        def what_color(self):
            return self.color
            
    ## клиентский код    
    cat = Animal('grey','20sm')
    print(cat.what_color())

В каждый метод передается обязательный (если метод не статический) параметр self, который представляет будущий объект.

С помощью self мы будем иметь доступ к свойствам объекта как в примере выше.

### Функция __str__

Каждый объект имеет свое строковое представление.

За него отвечает метод __str__.

Напимер этот метод скрыто использует оператор print при попытке вывести объект.

Это очень удобно при одладке.

Например такой код 

    class Mycl():
        pass
        
    m = Mycl()
    print(m)

Выведет 

    >>> <__main__.Mycl instance at 0x7ff704c8c488>
    
Что и будет строковым представлением объекта, которого требует оператор print.

Чтобы поменять это представление необходимо определить функцию __str__ в которой возвратить желаемую строку.    

    class Mycl():
        def __str__(self):
            return "This is my class"
        
    m = Mycl()
    print(m)
    
    >>> This is my class

### Пример наследования классов.


    class Car(object):

        def __init__(self):
            self.doors = 2

        def move(self):
            return 'dr-dr-dr-d'


    c = Car()
    print c.doors


    class Lorry(Car):

        def __init__(self):
            self.color = 'red'


    l = Lorry()
    print l.color
    print l.doors

Получаем ошибку:


    AttributeError: 'Lorry' object has no attribute 'doors'

Потому, что при наследовании мы потеряли свойство color.

Чтобы этого не происходило, необходимо вызвать конструктор родительского класса Car.

    def __init__(self):
        self.color = 'red'
        super(Lorry, self).__init__()


## Статические методы.

Наиболее часто-используемые методы классов - это методы объектов (экземпляров).

Что если нам не нужно оперировать экземпляром, а работать с самим классом?

Мы могли бы использовать просты функции. Наример:

    def get_no_of_instances(cls):
        return cls.cnt
     
    class Kls(object):
        cnt = 0
        def __init__(self):
            Kls.cnt = Kls.cnt + 1

     
    ik1 = Kls()
    ik2 = Kls()
     
    print(get_no_of_instances(Kls))
    
    >> 2
    
Но при таком подходе мы помещаем функцию, работающую с классом за за его пределами, что плохо для читабельности
и последующей поддержки.

Чтобы этого избежать используются статические методы классов, в которые не нужно передавать параметр экземпляра self.



## Декоратор @classmethod

Говорит о том, что мы хотим использовать метод как статический.


    class Kls(object):
        cnt = 0
     
        def __init__(self):
            Kls.cnt = Kls.cnt + 1
     
        @classmethod
        def get_cnt(cls):
            return cls.cnt
     
    ik1 = Kls()
    ik2 = Kls()
     
    print ik1.get_cnt()
    print Kls.get_cnt()
    
    >> 2


Преимущество такого подхода в том, что от куда бы мы не вызвали статический метод, из класса, или его экземпляра - всегда
в качестве первого аргумента будет передан сам класс.



