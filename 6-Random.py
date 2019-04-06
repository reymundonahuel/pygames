import pygame,sys
from pygame.locals import * 
from random import randint

pygame.init()  
ventana = pygame.display.set_mode((400,300)) 
pygame.display.set_caption("Tutorial Cinco")  


Mi_imagen = pygame.image.load("imagenes/dados.png")
posX= randint(10,300) ''' Pasamos valor en el que empieza y hasta donde se genera el numero random '''
posY= randint(10,200)

ventana.blit(Mi_imagen,(posX,posY))
print(posX,posY) ''' Mostramos la posicion aleatoria '''

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()