from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



question_list = [
    {'question': 'What is the capital of Poland?', 'name':'capital', 'answers': [
        {'text': '1. Krakow', 'statement': False, 'value':'Krakow'},
        {'text': '2. Warsaw', 'statement': True, 'value':'Warsaw'},
        {'text': '3. Wroclaw', 'statement': False, 'value':'Wroclaw'}
    ]},
    {'question': 'Choose the longest river in Ukraine.', 'name':'river', 'answers': [
        {'text': '1. Dniepr',  'statement': True, 'value':'Wroclaw'},
        {'text': '2. Dniestr', 'statement': False, 'value':'Wroclaw'},
        {'text': '3. Desna', 'statement': False, 'value':'Wroclaw'}
    ]},
    {'question': 'What is the smallest continent in the world?', 'name':'continent', 'answers': [
        {'text': '1. Europe', 'statement': False, 'value':'Wroclaw'},
        {'text': '2. South America', 'statement': False, 'value':'Wroclaw'},
        {'text': '3. Australia', 'statement': True, 'value':'Wroclaw'}
    ]}
]

def index(request): #GET

    return render(request, 'index.html', {'questions': question_list})

def test(request): #POST
    if request.method == 'POST':
        ### Проверить результаты и вывести оценку.
        print(request.POST.get('river'))
    return render(request, 'index.html', {'questions': question_list, 'var': 1})