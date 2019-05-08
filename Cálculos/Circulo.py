from Puntos import *
from Figuras import *

class Circulo(Figuras):
    
    def calculararea(self):
        self.area = math.pi * ((self.p1.distancia(self.p2))**2)

    def calcularperimetro(self):
        self.perimetro = 2 * math.pi * (self.p1.distancia(self.p2))
   

