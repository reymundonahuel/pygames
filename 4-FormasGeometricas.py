import pygame,sys
from pygame.locals import * 

pygame.init()  
ventana = pygame.display.set_mode((400,300)) 
pygame.display.set_caption("Hola Mundo")

color = pygame.Color(80,70,120)
color2 = pygame.Color(150,50,30)
color3 = pygame.Color(220,10,30)

''' Dibujar un circulo '''
pygame.draw.circle(ventana,color,(80,90),20)
''' Dibujar un rectangulo '''
pygame.draw.rect(ventana,color2,(0,0,100,50))
''' Dibujar un poligono '''
pygame.draw.polygon(ventana,color3,((80,90),(150,100),(40,80),(60,80)))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()