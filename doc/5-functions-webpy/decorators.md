## Декораторы

Декораторы - это такая конструкция языка, которая может изменить поведение функции, метода, класса и т.д. не изменяя ее саму.

Это идеальный способ что то изменить в программе без модификации кода изменяемого объекта.

Разберем процесс декорирования функции.

Для начала, рассмотрим некоторые особенности функций.


### Присвоение функции переменной.

    def greet(name):
        return "hello "+name

    greet_someone = greet
    print greet_someone("John")

    # Outputs: hello John

Как видно, функция может быть присвоена переменной как обычное значение и следовательно быть передана как параметр другой функции.

### Определение функции внутри другой функции.

    def greet(name):
        def get_message():
            return "Hello %s" % name
        result = get_message()+'!'
        return result
    print greet("John")

    # Outputs: Hello John

При определении внутренней функции все переменные, переданные во внешнюю, буду сохранены во внутреннем пространстве (замыкании)
внешней функции и доступны из внутренней.

### Передача функции как параметра другой функции.


    def greet(name):
       return "Hello " + name 

    def call_func(func):
        other_name = "John"
        return func(other_name)  

    print call_func(greet)

    # Outputs: Hello John

Функция может быть передана параметром и быть вызвана изнутри той функции, в которую была передана.

### Функция может возвращать другую функцию.

Иными словами - функция может создавать функцию.

    def compose_greet_func():
        def get_message():
            return "Hello there!"

        return get_message

    greet = compose_greet_func()
    print greet()

    # Outputs: Hello there!


### Внутрення функция имеет доступ к замыкающему пространству имен внешней.

    def compose_greet_func(name):
        def get_message():
            return "Hello there "+name+"!"

        return get_message

    greet = compose_greet_func("John")
    print greet()

    # Outputs: Hello there John!

Обратите внимание на то как мы забираем переменную name из замыкания и возвращаем внутреннюю функцию.

В момент вызова **greet = compose_greet_func("John")** в greet будет находится строка "John".

### Декоратор.

Давайте совместим идеи, изложенные выше и построим декоратор.

Putting the ideas mentioned above together, we can build a decorator.
In this example let's consider a function that wraps the string output of another function by p tags.

В примере предположим, что нам необходимо изменить вывод функции get_text, заключив
ее вывод в тэги <p></p>.

    def get_text(name):
       return "Hello, {0}".format(name)

    def p_decorate(func):
       def func_wrapper(name):
           return "<p>{0}</p>".format(func(name))
       return func_wrapper

    my_get_text = p_decorate(get_text)

    print my_get_text("John")

    # <p>Hello, John</p>

Это и был наш первый декоратор.
Т.е. функция-декоратор, принимающаю другую (декорируемую) функцию в качестве аргумента и изменяющая ее поведение.
Поведение изменяется внутри вложенной функции декоратора строкой **return "<p>{0}</p>".format(func(name))**.
При этом мы вызываем декорируемую функцию в том месте, где хотим получить ее результат.
В конце возвращаем эту вложенную функцию, которая называется оберткой (wrapper).

### Синтаксис декоратора в Python.

Применение декоратора может быть упрощено использованием знака @.

Этот знак - эквивалент процедуры **my_get_text = p_decorate(get_text)** из примера выше.

    def p_decorate(func):
       def func_wrapper(name):
           return "<p>{0}</p>".format(func(name))
       return func_wrapper

    @p_decorate
    def get_text(name):
       return "lorem ipsum, {0} dolor sit amet".format(name)

    print get_text("John")

    # Outputs <p>lorem ipsum, John dolor sit amet</p>

Now let's consider we wanted to decorate our get_text function by 3 other functions.

Теперь представим, что нам нужно задекорировать не одной а тремя функциями последовательно, добавив дополнительные теги strong и div.

Определим эти три функции-декоратора.

    def p_decorate(func):
       def func_wrapper(name):
           return "<p>{0}</p>".format(func(name))
       return func_wrapper

    def strong_decorate(func):
        def func_wrapper(name):
            return "<strong>{0}</strong>".format(func(name))
        return func_wrapper

    def div_decorate(func):
        def func_wrapper(name):
            return "<div>{0}</div>".format(func(name))
        return func_wrapper

With the basic approach, decorating get_text would be along the lines of

При стандартном подходе, чтобы задекорировать всеми тремя нужно выполнить такой код:

    get_text = div_decorate(p_decorate(strong_decorate(get_text)))

Однако при использовании синтаксиса декоратора Python это можно написать гораздо проще и понятней.


    @div_decorate
    @p_decorate
    @strong_decorate
    def get_text(name):
       return "lorem ipsum, {0} dolor sit amet".format(name)

    print get_text("John")

    # Outputs <div><p><strong>lorem ipsum, John dolor sit amet</strong></p></div>


### Декораторы с аргументом.

Что если нам нужно менять тег, в который мы помещаем вывод декорируемой функции из примеров выше.

Очевидно, для этого тег необходимо передавать в качестве параметра декоратору:

    def decorator(opentag,closetag):

        def real_decorator(decfunc):
        
            def wrapper(name):
                
                return opentag+' '+ decfunc(name) +' '+closetag
                
            return wrapper
            
        
        return real_decorator
       
       
В таком случае, при декорировании, передаем эти параметры:       
       
    @decorator('<h1>','</h1>') 
    def myf(name):
        return name
        
        
    print myf('Dima')













