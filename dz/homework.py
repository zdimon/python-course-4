#!/usr/bin/env python3
def greet():
    print("Enter your name please.") 

greet()


name = input()
print('Hello, %s! Test your geography knowledge.' % name)


question_list = [
    {'question': 'What is the capital of Poland?', 'answers': [
        {'text': '1. Krakow', 'statement': False},
        {'text': '2. Warsaw', 'statement': True},
        {'text': '3. Wroclaw', 'statement': False}
    ]},
    {'question': 'Choose the longest river in Ukraine.', 'answers': [
        {'text': '1. Dniepr',  'statement': True},
        {'text': '2. Dniestr', 'statement': False},
        {'text': '3. Desna', 'statement': False}
    ]},
    {'question': 'What is the smallest continent in the world?', 'answers': [
        {'text': '1. Europe', 'statement': False},
        {'text': '2. South America', 'statement': False},
        {'text': '3. Australia', 'statement': True}
    ]}
]


answ = 'yes'
while answ == 'yes':
    corr_answ = 0
    for q in question_list:
      print(q['question'])
      for a in q['answers']:
        print(a['text'])
      answer = int(input())
      clue = q['answers']
      if clue[answer-1]['statement'] == True:
        print('You are right, %s.' % name)
        corr_answ += 1
      else:
        print('%s, you are wrong.' % name)


    if (corr_answ == 1):
      print(f'Your result is {corr_answ} out of 3. You can better.')
    elif (corr_answ == 2):
      print(f'Your result is {corr_answ} out of 3. Not bad.')
    else:
      print(f'Your result is {corr_answ} out of 3. You are amazing!')
    

    print('Do you want try again? (yes/no)')

    answ = input()

    if answ == 'no':
      print(f'Bye, {name}!')