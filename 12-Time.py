import pygame,sys
from pygame.locals import * 

pygame.init()  
ventana = pygame.display.set_mode((400,300)) 
pygame.display.set_caption("Hola Mundo") 

fuente = pygame.font.SysFont("Arial",30)

aux=1

while True:
    ventana.blit(Mi_Imagen,)
    ventana.fill((255,255,255))
    tiempo = pygame.time.get_ticks()/1000 ''' Valor en milisegundos de tipo entero ''' ''' Devuelve tiempo transcurrido desde que se inicio pyinit '''
    if aux == tiempo:
        aux+=1
        print(tiempo)


    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    contador = fuente.render("Tiempo es:" + str(tiempo),0,(127,50,50),None)
    ventana.blit(contador,(100,100))
    pygame.display.update()