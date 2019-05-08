from Figuras import *

class Rectangulo(Figuras):

    def arearec(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = p3.distancia(self.p1) * p3.distancia(self.p2)

    def perimetrorec(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.perimetro = 2*p3.distancia(self.p1) + 2*p3.distancia(self.p2)
   
