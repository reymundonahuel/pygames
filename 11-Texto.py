import pygame,sys
from pygame.locals import * 

pygame.init()  
ventana = pygame.display.set_mode((400,300)) 
pygame.display.set_caption("Tutorial Once")  

miFuente= pygame.font.Font(None,30)
miTexto = miFuente.render("Prueba Fuente",0,(255,255,255),(100,70,120)) 
miFuente2 = pygame.font.SysFont("Arial",30)
miTexto2 = miFuente2.render("Prueba Fuente 2",0,(255,255,255),(100,70,120)) 

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    ventana.blit(miTexto2,(200,200))
    ventana.blit(miTexto,(100,100))
    pygame.display.update()