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

        # Selecciono un punto del array de puntos.
        puntoRandom = listaDePuntos.get(r.randint(0, listaDePuntos.size() - 1))
        # Selecciono unos de los vertices del triángulo.
        puntoRandomTriangulo = triangulo.get(r.randint(0, triangulo.size() - 1))

        # Creo un objeto Recta con los puntos seleccionados.
        recta = Recta(puntoRandom, puntoRandomTriangulo)

        # Calculo la posición del punto intermedio.
        x = ((puntoRandom.posX + puntoRandomTriangulo.posX) / 2)
        y = recta.getOrdenada(x)
        puntoIntermedio = Punto(x, y)

        # Dibujo el punto.
        pygame.draw.circle(screen, black, puntoIntermedio.getCoordenadas(), radio)

        # Appendeo el punto a la lista de puntos.
        listaDePuntos.append(puntoIntermedio)

        pygame.display.flip()



    



    
    