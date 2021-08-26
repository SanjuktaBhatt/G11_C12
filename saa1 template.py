import pygame
pygame.init() 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Racing Game")
carryOn = True
#Load the images






while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False
    screen.fill((0,0,255))
    #Display the images
    
    
    
    
    
pygame.quit()
