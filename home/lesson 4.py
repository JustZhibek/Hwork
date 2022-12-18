# getter setter(менять защищенные методы)
# @property setter
# множественное наследование (MRO)

class O:
class A(O):
class B(O):
class C(O):
class D(O):
class E(O):
class K1(A, B, C):
class K2(B, D):
class K3(C, D, E):
class Z(K1, K2, K3):


print(Z.mro())


class One:
    def __init__(self, name):
        self.name = name


class Tho(One):
    def f(self):
        print('это функ Tho')


class Tho2(One):
    def f(self):
        print('это функ Tho')

    def tho2(self):
        print('это функ Tho')


class Three(Tho, Tho2): ...


h = Three('hello')
h.f()
h.tho2()
