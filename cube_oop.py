from random import randint


class wuerfel:
    def __init__(self):
        self.eyes = randint(1, 6)

        print(self.eyes)

    def throw(self):
        self.eyes = randint(1, 6)

        print(self.eyes)


cube1 = wuerfel()

while cube1.eyes != 6:
    cube1.throw()
