import pygame
import random
#Import time module
import time

pygame.init()

size = (350, 400)
screen = pygame.display.set_mode(size)
carx=60
cary=340
threshold=0
roadx=-10
roady=0
threshold=0
#Create a counter variable
counter=0


#Replace file location address on your computer
road=pygame.image.load("Assets/Road.png").convert_alpha()
road=pygame.transform.smoothscale(road,(400,800))

#Replace file location address on your computer
car=pygame.image.load("Assets/Car.png").convert_alpha()
car=pygame.transform.smoothscale(car,(70,60))

carryOn = True

#Create timepoint t1 here
t1=time.time()


while carryOn:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False
  
  screen.blit(road,(roadx,roady))
  screen.blit(car,(carx,cary))
  
  

  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_UP:
        cary-=2
        roady-=1
    if event.key==pygame.K_DOWN:
        cary+=2
    if event.key==pygame.K_LEFT:
        carx-=2
    if event.key==pygame.K_RIGHT:
        carx+=2

  if cary<=0:
    #Increment counter by 1
    counter+=1
    roady=0
    cary=340
  
  
  #Create second time point here
  t2=time.time()
  #Evaluate gametime here
  game_time=t2-t1
  game_time=round(game_time,2)
  
  #Display gametime here
  #Select font
  font = pygame.font.Font(None, 24)
  #Select text.Remember to concatenate gametime
  text = font.render("TIME ELAPSED: " + str(game_time)+"seconds", 1, (255,0,255))
  #Display the text
  screen.blit(text, (50,10))
  
  #Check if Key is pressed
  if event.type==pygame.KEYDOWN:
  #Check if key pressed is "Enter"
        if event.key==pygame.K_RETURN:
        #Check if game time is within threshold
            if game_time>=threshold and game_time<=(threshold+10):
                    #Decrement "cary" to make car move forward
                    cary-=10 
                    #Increment "threshold" by 10
                    threshold+=10
  
  
  #check if counter is equal to 100
  if counter>=5:
    #Create the finish line rectangle
    finishline=pygame.Rect(50,40,240,20)
    #Draw the rectangle
    pygame.draw.rect(screen,(255,255,255),finishline)
    font = pygame.font.Font(None, 20)
    text = font.render("FINISH", 1,(255,0,0))
    screen.blit(text, (150,40))
  pygame.display.flip()
  
pygame.quit()
