import Punto as p

class Recta:

    def __init__(self, puntoA, puntoB):
        self.m = None
        self.ordenadaAlOrigen = None
        self.setFunction(puntoA, puntoB)
        
    def setFunction(self, puntoA, puntoB):
        
        '''
        y - y1 = m * (x - x1)
        m = y2 - y1 / x2 - x1

        y = (m * x - m * x1) + y1
        '''

        if (puntoA.posX > puntoB.posY):
            y1 = puntoB.posY
            y2 = puntoA.posY
            x1 = puntoB.posX
            x2 = puntoA.posX
        else:
            y1 = puntoA.posY
            y2 = puntoB.posY
            x1 = puntoA.posX
            x2 = puntoB.posX

        #print(f"X1:{x1} Y1:{y1} // X2:{x2} Y2:{y2}")

        if (x2 != x1):
            self.m = ((y2 - y1) / (x2 - x1))
        else:
            self.m = 0

        self.ordenadaAlOrigen = (self.m * x1 - y1)

    def getStringFormula(self):

        return (f"y = {self.m} * x - ({self.ordenadaAlOrigen})")

    def getOrdenada(self, x):
        y = (self.m * x) - (self.ordenadaAlOrigen)
        return y