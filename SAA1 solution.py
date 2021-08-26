import pygame
pygame.init() 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Racing Game")
carryOn = True
#Load the images
tree_location="C:/Users/dell/Documents/img/tree.png"
treeImg=pygame.image.load(tree_location).convert_alpha()
hut_location="C:/Users/dell/Documents/img/hut.png"
hutImg=pygame.image.load(tree_location).convert_alpha()
cloud_location="C:/Users/dell/Documents/img/cloud.png"
cloudImg=pygame.image.load(tree_location).convert_alpha()

while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False
    screen.fill((0,0,255))
    #Display the images
    screen.blit(treeImg,[0,400])
    screen.blit(cloudImg,[20,300])
    screen.blit(cloudImg,[20,250])
    screen.blit(hutImg,[300,400])
pygame.quit()
