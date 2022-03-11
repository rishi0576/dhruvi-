import pygame
pygame.init()

screen = pygame.display.set_mode((400,600))

player = pygame.Rect(200,500,30,30)
enemy  = pygame.Rect(350,500,1000,1000)

while True:
     screen.fill((0,0,0))
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()     
            
     pygame.draw.rect(screen,(0,255,0),player)
     pygame.draw.rect(screen,(255,0,0),enemy)
     pygame.display.update()        
     