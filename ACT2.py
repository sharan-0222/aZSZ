import pygame 
pygame.init()
done=False
screen=pygame.display.set_mode((400,500))
green=(0,255,0) 
screen.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.circle(screen,green,(200,250),50)
    pygame.draw.circle(screen,green,(122,90),50,5)
    pygame.display.flip()
pygame.quit()