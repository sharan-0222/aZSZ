import pygame 

pygame.init()
done=False
screen=pygame.display.set_mode((400,500))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(200,100,200),(20,0,60,60))

    pygame.display.flip()