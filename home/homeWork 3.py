class Bank:
    def __init__(self, name='zhik', balance=100):
        self._name = name
        self._balance = balance

    def moneyX(self):
        a = int(input('Добавьте денег'))
        return self._balance + a

    def _kill(self):
         self._balance = 0

    def __jackpot(self):
        return self._balance * 10

    def _add(self, other):
        return self.balance + other.balance


b = Bank()
print(b._name)
print(b._balance)
print(b.moneyX())
print(b._kill)
print(b.__jackpot)
