import math

class Punto ():
    
    def __init__(self):
        
        self.x = 0
        self.y = 0
        
    def distancia (self,punto):
       return math.sqrt((self.x-punto.x)**2 +(self.y-punto.y)**2)
   
    
