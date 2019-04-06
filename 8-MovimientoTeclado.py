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
velocidad=5

while True:
    ventana.fill(blanco)
    ventana.blit(Mi_imagen,(posX,posY))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                posX -= velocidad
            elif event.key == K_RIGHT:
                posX += velocidad
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                print("Tecla Izquierda")
            elif event.key == K_RIGHT:
                print("Tecla Derecha")



        pygame.display.update()