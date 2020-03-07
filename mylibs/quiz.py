
def add(*args):
    accum = 0 
    for i in args:
        accum += i
        #print(i)
    

    def hello():
        print("Hello") 

    hello()

    return accum




def quiz(user_name):
    print('Hello %s!!!!!' % user_name)
    value = 0

    question_list = [
        {'question': 'What is your name??', 'answers': [
            {'text': '1. Dima', 'true': True},
            {'text': '2. Yulia', 'true': False}
        ]},
        {'question': 'How old are you?', 'answers': [
            {'text': '1. 30',  'true': True},
            {'text': '2. 40', 'true': False}
        ]}
    ]


    for q in question_list:
        print(q['question'])
        for a in q['answers']:
            print(a['text'])
        answer = int(input())
        el = q['answers'][answer-1]
        if el['true'] == True:
            print('You are right!!!')
            value +=  10
        else:
            print('You are WRONG!!!')



    print("You have got %s %s" % (value,value))
    return True