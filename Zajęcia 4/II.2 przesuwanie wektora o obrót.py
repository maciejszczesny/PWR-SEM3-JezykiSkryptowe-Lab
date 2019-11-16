import math

class wektor(object):
    def __init__(self, x=1,y=1):
        self.x=x
        self.y=y
    def dlugosc(self):
        return math.hypot(self.x,self.y)
    def __add__(self,other):
        return wektor(self.x+other.x, self.y+other.y)
    def __str__(self):
        return ("Wektor(%g,%g)" % (self.x,self.y))
    def __repr__(self):
        return ("Wektor(%g,%g)" % (self.x,self.y))
    def obrot(self,kat): #obrót o radiany
        #kat = math.radians(kat) rozdzielenie do osobnej funkcji
        self.x,self.y = self.x*math.cos(kat)-self.y*math.sin(kat),self.x*math.sin(kat)+self.y*math.cos(kat)
    def obrot_stopnie(self,kat): #obrót o stopnie
        self.obrot(math.radians(kat))

w1 = wektor()
w2 = wektor(2,2)
w3 = w1+w2
print('wektor w1=', w1, 'ma długość', w1.dlugosc())
print('wektor w2=', w2, 'ma długość', w2.dlugosc())
print('wektor w3=', w3, 'ma długość', w3.dlugosc())

w1.obrot(2*math.pi)
print('obrócony o 2*PI wektor w1=', w1, 'ma długość', w1.dlugosc())
w1.obrot_stopnie(360)
print('obrócony o 360 stopni wektor w1=', w1, 'ma długość', w1.dlugosc())
w1.obrot(1/2*math.pi)
print('obrócony o 1/2*PI wektor w1=', w1, 'ma długość', w1.dlugosc())
w1.obrot(3/2*math.pi) #zerowanie do 1,1
print('obrócony o 3/2*PI wektor w1=', w1, 'ma długość', w1.dlugosc())
w1.obrot_stopnie(90)
print('obrócony o 90 stopni wektor w1=', w1, 'ma długość', w1.dlugosc())
