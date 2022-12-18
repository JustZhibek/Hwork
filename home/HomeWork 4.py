class Mammals:
    def __init__(self, name):
        self.name = name


class Lion:
    def __init__(self, age):
        self.age = age


class Cat(Mammals):
    def tail(self):
        print('хвостик')


class Dog(Lion):


    def teeth(self):
        print('зубки')


class Wolf(Cat, Dog):...


w=Wolf('Balto')
w.tail()
w.teeth()
