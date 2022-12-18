class Mammals:
    def __init__(self, name):
        self.name = name
class Lion:
    def __init__(self, age):
        self.age = age
class Cat:
    def tail(self):
        print('хвостик')
class Dog:
    def teeth(self):
        print('зубки')
class Wolf(Mammals,Lion,Cat, Dog):
    def __init__(self, name, age):
         Mammals.__init__(self, name)
         Lion.__init__(self, age)


w = Wolf('Balto', 18)
w.tail()
w.teeth()