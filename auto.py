
class car(object):
    def __init__(self, model, color, hp, vmax):
        self.color = color
        self.hp = hp
        self.vmax = vmax

        self.v = 0

    def changespeed(self,v):
        self.v += v

        print(self.v)


    def showspeed(self):

        print(self.v)



auto1 = car("ferrari", "rot", 100,200)

auto1.changespeed()
auto1.showspeed()
