import math

class Punkt():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Punkt(self.x+other.x, self.y+other.y)
    def odleglosc(self):
        return math.hypot(self.x,self.y)
    def dystans(self,external):
        return math.hypot(external.x-self.x,external.y-self.y)
    def __str__(self):
        return ("Punkt(%g,%g)" % (self.x,self.y))
    def __repr__(self):
        return ("(%g,%g)" % (self.x,self.y))
p1 = Punkt(1,0)
p2 = Punkt(55,0)
print(p1)
print(p2)
print(p1.dystans(p2))
