from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

question_list = [

    {'question': 'What is your name??', 'answers': [
        {'text': '1. Dima', 'true': True},
        {'text': '2. Yulia', 'true': False}
    ]},
    {'question': 'How old are you?', 'answers': [
        {'text': '1. 30',  'true': True},
        {'text': '2. 40', 'true': False}
    ]},
   
]


def index(request):
    print('My index')
    return render(request,'index.html', {'name': 'Dima', 'quiz': question_list})

def index2(request):
    print('My index')
    return HttpResponse('<h1>Hello 2</h1><a  href="/">Main</a>')