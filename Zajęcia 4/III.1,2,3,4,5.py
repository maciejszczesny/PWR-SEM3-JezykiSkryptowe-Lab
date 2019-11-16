import math

class Punkt():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Punkt(self.x+other.x, self.y+other.y)
    def odleglosc(self):
        return math.hypot(self.x,self.y)
    def dystans(self,ext):
        return math.hypot(ext.x-self.x,ext.y-self.y)
    def __str__(self):
        return ("Punkt(%g,%g)" % (self.x,self.y))
    def __repr__(self):
        return ("(%g,%g)" % (self.x,self.y))
class Kolo(Punkt):
    def __init__(self, x=Punkt().x,y=Punkt().y,r=1):
        self.x = x
        self.y = y
        self.r = r
    def obwod(self):
        return 2*math.pi*self.r
    def pole(self):
        return math.pi*self.r**2
    def __str__(self):
        return ("Koło(%g,%g,%g)" % (self.x,self.y,self.r))
    def __repr__(self):
        return ("(%g,%g,%g)" % (self.x,self.y,self.r))
    def przesun(self,wektor):
        self.x += wektor[0]
        self.y += wektor[1]
    def cz_wsp(self,ext):
        return True if self.dystans(ext)-self.r-ext.r <=0 else False



