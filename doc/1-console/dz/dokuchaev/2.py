#! /usr/bin/env python
# -*- coding: utf-8 -*-

questions = [ 
        {
            "question": "Оператор вывода на экран?", 
            "answers": [
                {"text": "1 echo", "is_true": False},
                {"text": "2 print", "is_true": True},
                {"text": "3 output", "is_true": False}
            ] 
        },

        {
            "question": "Оператор цикла?", 
            "answers": [
                {"text": "1 for", "is_true": True},
                {"text": "2 if", "is_true": False},
                {"text": "3 loop", "is_true": False}
            ]
        },

    ]

for i in questions:
    print("\x1b[34;47m" + i["question"] + "\x1b[0m")
    for j in i["answers"]:
        print("\x1b[34;47m" + j["text"] + "\x1b[0m")

    value = input("Укажите правильный номер: ")
    value = int(value)
    print("---------------------")
    if i["answers"][value - 1]["is_true"] == True:
        print('\x1b[30;42m' + 'Верно!' + '\x1b[0m')
    else:
        print('\x1b[30;41m' + 'Не верно!' + '\x1b[0m')
    print("---------------------")
