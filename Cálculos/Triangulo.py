from Puntos import *
from Figuras import *

class Triangulo(Figuras):

    def areatri(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = (p3.distancia(self.p1) * p3.distancia(self.p2))/2

    def perimetri(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.perimetro = (2*p3.distancia(self.p1) + 2*p3.distancia(self.p2))/2
   



