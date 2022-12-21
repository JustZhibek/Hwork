class Hero:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


class Hero_super(Hero):
    def __init__(self, name, ability):
      Hero.__init__(self, name, ability)
    def __str__(self):
        return f'{self.name} it is super_hero'

h=Hero_super('Master','supervision')
print(h)