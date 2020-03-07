
import time


class Canjump():

    def jump(self):
        print('I can jump')


class CanNotjump():

    def jump(self):
        print('I can NOT jump')





class Animal():
    width = '10kg'
    color = 'red'
    age = 10
    x = 0
    y = 0
    
    
    def __init__(self, canjump):
        if canjump == 'yes':
            self.jumpclass = Canjump()
        else:
            self.jumpclass = CanNotjump()



        print('Creation!!!!!')

    def walk(self):
        for i in range(0,10):
            self.x = self.x + 10
            # time.sleep(1)
            print('top to x= %s' % self.x)


    def jump(self):
        self.jumpclass.jump()
        

class Dog(Animal):


    def sound(self):
        print('gav gav i am %d' % self.age)




class Cat(Animal):

    def sound(self):
        print('mayy i am %d' % self.age)


