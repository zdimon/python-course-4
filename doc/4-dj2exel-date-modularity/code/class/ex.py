#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
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
'''


class User(object):
    """docstring - a simple example class"""
    name = 'Dima'
    def say_name(self):
        print('my name is %s' % self.name)


user = User()
user.name
user.say_name()