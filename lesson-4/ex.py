import json

bd = {
    'users': [
        {'id': 1, 'name': 'Dima', 'age': 345},
        {'id': 2, 'name': 'Vova', 'age': 23}
    ],
    'messages': [
        {'text': 'Hello', 'user_id': 2},
        {'text': 'Hello2', 'user_id': 2}
    ],
    'books': [
        {'id': 1, 'title': 'World'},
        {'id': 2, 'title': 'World 2'}
    ],
    'book2user': [
        {'user_id': 1, 'book_id': 2},
        {'user_id': 2, 'book_id': 2}
    ]
}



def save_bd(bd):
    file = open('bd.json','w')
    file.write(json.dumps(bd))
    file.close()
    print('Done')

def read_db(name):
    file = open(name,'r')
    out = json.loads(file.read())
    print(out['users'])


dsvsdvsd
def outer():
    def inner(name):
        return 'Hello %s' % name
    return inner


def hello(oterfunc):
    oterfunc()

def oterfunc():
    print('asfasfasfsafaws')


hello(oterfunc)

#myf = outer()
#print(myf('Dima'))





#read_db('bd.json')
#save_bd(bd)




# def myf(*args,**kwargs):

#     print(kwargs['name'])
#     # print(args[1])

#     for i in args:
#         if i==2: 
#             print(i)


# myf(1,2,3,4, name='Dima', age=23)

# #myf('URAAAAA')