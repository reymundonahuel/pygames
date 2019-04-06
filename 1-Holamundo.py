import pygame,sys
from pygame.locals import * ''' Importamos librerias pygame y sys '''

pygame.init()  ''' Inicializamos pygame '''
ventana = pygame.display.set_mode((400,300)) ''' Colocamos el tamaño de la ventana '''
pygame.display.set_caption("Hola Mundo")  ''' Colocamos el titulo de la ventana '''

''' Mientras sea verdadero (infinite loop), nos fijamos que al apretar la X, se cierre la ventana '''
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

''' Actualizamos la ventana ''' 
        pygame.display.update()