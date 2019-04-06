import pygame,sys
from pygame.locals import * 


pygame.init()  
ventana = pygame.display.set_mode((800,800)) 
pygame.display.set_caption("Tutorial Diez")  


rectangulo_2 = pygame.Rect(200,300,100,50)
posX= 200
posY= 100


blanco=(255,255,255)
velocidad=2
derecha = True
rectangulo = pygame.Rect(0,0,100,50)

if rectangulo.colliderect(rectangulo_2):
    velocidad = 0
    print("Colisiono")

while True:
    ventana.fill(blanco)
    pygame.draw.rect(ventana,(180,70,70),rectangulo_2)
    pygame.draw.rect(ventana,(180,70,70),rectangulo)
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
       
    if derecha == True:
        if posX<400:
            posX+=velocidad
            rectangulo_2.left = posX
        else:
            derecha = False
    else:
        if posX>1:
            posX-=velocidad
            rectangulo_2.left = posX
        else:
            derecha = True


        pygame.display.update()