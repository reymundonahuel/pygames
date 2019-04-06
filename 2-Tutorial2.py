''' Colores RGB
Van desde el 0 hasta el 255 = 0-255
RGB(120,40,90) 120= Cantidad de Rojo
               40 = Cantidad de Verde
               90 = Cantidad de Azul

 '''

import pygame,sys
from pygame.locals import * 
''' Creando colores '''
color = (0,140,60)
colorDos = pygame.Color(255,120,9)


pygame.init()  
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")  

while True:
    ventana.fill(colorDos) 
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()