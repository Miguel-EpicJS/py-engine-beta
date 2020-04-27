import pygame#import pygame

pygame.init()#iniciando pygame

SCREEN_WIDTH = 800#largura
SCREEN_HEIGHT = 400#altura
#*****CONFIGURANDO*JANELA*****#
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My engine")
#************************************************************#
comand = pygame.key.get_pressed()

def createAndMoveRect(x,y,width,height,vel):
    screen.fill((255,255,255))

    pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    if comand[pygame.K_RIGHT]:
        x += vel
    if comand[pygame.K_LEFT]:
        x -= vel
    if comand[pygame.K_UP]:
        y += vel
    if comand[pygame.K_DOWN]:
        y -= vel

while True:
    pygame.time.delay(100)
    createAndMoveRect(50,50,40,60,5)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
