import random as r, pygame, sys, time
from Punto import Punto
from Recta import Recta
from ArregloDePuntos import ArregloDePuntos

pygame.init()

# Ventana
size = width, height = 600, 600
speed = [2, 2]
white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Triangulo")

# Triángulo
margen = 70
verticeA = Punto((width / 2), margen)
verticeB = Punto(margen, height - margen)
verticeC = Punto(width - margen, height - margen)
triangulo = ArregloDePuntos()
triangulo.append(verticeA)
triangulo.append(verticeB)
triangulo.append(verticeC)

# Puntos
radio = 2
puntoInicial = Punto(400, 400)
listaDePuntos = ArregloDePuntos()
listaDePuntos.append(puntoInicial)

# Flags
flag = True
dibujo = True

while flag:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Printeo la ventana y el triángulo.
    screen.fill(white)
    pygame.draw.polygon(screen, black, triangulo.getArrregloDeCoordenadas(), width=5)

    while dibujo:

        # Seleciono un punto del array de puntos.
        puntoRandom = listaDePuntos.get(r.randint(0, listaDePuntos.size() - 1))
        puntoRandomTriangulo = triangulo.get(r.randint(0, triangulo.size() - 1))

        recta = Recta(puntoRandom, puntoRandomTriangulo)

        x = ((puntoRandom.posX + puntoRandomTriangulo.posX) / 2)
        y = recta.getOrdenada(x)

        puntoIntermedio = Punto(x, y)

        for i in listaDePuntos.arregloDePuntos:
            pygame.draw.circle(screen, black, i.getCoordenadas(), radio)

        listaDePuntos.append(puntoIntermedio)

        #time.sleep(0.2)

        pygame.display.flip()



    



    
    
