from Puntos import *
from Rectangulo import *
from Circulo import *
from Triangulo import *
from Cuadrado import *

p1=Punto()
p2=Punto()
p1.x = input ("Ingrese coordenada x del punto 1")
p1.x = input ("Ingrese coordenada y del punto 1")
p2.y = input ("Ingrese coordenada x del punto 2")
p2.y = input ("Ingrese coordenada y del punto 2")

r = Rectangulo()
r.setPuntos(p1,p2)
r.arearec()
r.perimetrorec()
print r.area, r.perimetro

t = Triangulo()
t.setPuntos(p1,p2)
t.areatri()
t.perimetri()
print t.area, t.perimetro

c = Circulo()
c.setPuntos(p1,p2)
c.areacir()
c.perimetrocir()
print c.area, c.perimetro

s = Cuadrado()
s.setPuntos(p1,p2)
s.areacua()
s.perimetrocua()
print s.area, s.perimetro

print r.area, r.perimetro
print t.area, t.perimetro
print c.area, c.perimetro
print c.area, c.perimetro


