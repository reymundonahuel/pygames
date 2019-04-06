import pygame,sys
from pygame.locals import * 


pygame.init()  
ventana = pygame.display.set_mode((800,800)) 
pygame.display.set_caption("Tutorial Cinco")  


Mi_imagen = pygame.image.load("imagenes/dados.png")
posX= 200
posY= 100

ventana.blit(Mi_imagen,(posX,posY))
blanco=(255,255,255)
velocidad=2

while True:
    ventana.fill(blanco)
    ventana.blit(Mi_imagen,(posX,posY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if posX < 300 and posX > 1:
        posX += velocidad
    else:
        velocidad = -velocidad
        posX += velocidad


        pygame.display.update()