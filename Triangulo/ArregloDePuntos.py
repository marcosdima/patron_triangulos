class ArregloDePuntos:

    def __init__(self):
        self.arregloDePuntos = []

    def append(self, punto):
        self.arregloDePuntos.append(punto)

    def getArrregloDeCoordenadas(self):
        retorno = []
        for i in (self.arregloDePuntos):
            retorno.append((i.posX, i.posY))
        return tuple(retorno)

    def get(self, i):
        return self.arregloDePuntos[i]

    def size(self):
        return len(self.arregloDePuntos)