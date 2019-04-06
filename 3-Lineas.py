import pygame,sys
from pygame.locals import * 

pygame.init()  
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Tutorial Cuatro")  
''' Trabajando con pixeles '''
color = pygame.Color(70,80,150)
'''' Dibujar una linea '''
pygame.draw.line(ventana,color,(60,80),(160,100),8) '''1er valor: Donde se va a dibujar; 2do valor: el color de la linea
                                                     3er valor: Donde empieza la linea; 4to valor: Donde termina
                                                     5to valor: Ancho de la linea'''


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()