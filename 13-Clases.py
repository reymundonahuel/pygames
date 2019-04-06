import pygame,sys
from pygame.locals import * 
#Variable globales
ancho = 900
alto = 480

class naveEspacial(pygame.sprite.Sprite):
    """ Clase para las naves """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imagenes/Clases/nave.jpg")
        self.rect = self.imagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30
        self.listaDisparo = []
        self.Vida = True

    def disparar(self):
        pass

    def dibujar(self, superficie):
        superficie.blit(self.imagenNave, self.rect)


def spaceInvader():
    pygame.init()  
    ventana = pygame.display.set_mode((ancho, alto)) 
    pygame.display.set_caption("Space Invader")
    ImagenFondo = pygame.image.load("imagenes/Clases/Fondo.jpg")  

    jugador = naveEspacial()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        ventana.blit(ImagenFondo,(0,0))        
        jugador.dibujar(ventana)
        pygame.display.update()
spaceInvader() 