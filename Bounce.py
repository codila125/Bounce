import pygame   #importing pygame library
pygame.init()   #initializing pygame

from pygame import mixer
mixer.init()
Strike = mixer.Sound("/Users/prabesh/Documents/Github/Bounce/app_media/Strike.wav")
Shot = mixer.Sound("/Users/prabesh/Documents/Github/Bounce/app_media/Shot.wav")
End = mixer.Sound("/Users/prabesh/Documents/Github/Bounce/app_media/End.wav")

import random

surface = pygame.display.set_mode((360, 720))     #setting the size of the game window and also making it resizable

pygame.display.set_caption("Bounce")     #Setting the title of our game window
Icon = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Icon.png")      #Loading image first before setting it
pygame.display.set_icon(Icon)   #Setting an icon of the game window

rocketsize = 50
vel = 15
rocketx = 180
rockety = 670
rockethealth = 100
healthbar = 0
rocket_img = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Rocket.png")
rocket_img = pygame.transform.scale(rocket_img,(rocketsize,rocketsize))

monster_img = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Space Monster.png")
monster_img = pygame.transform.scale(monster_img, (250,170))

bulletsize = 10
bulletx = random.randint(0, 360-bulletsize)
bullety = 150
bullet_img = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (bulletsize,bulletsize))

running = True
while running:  #keep game running till running is true

    for event in pygame.event.get():    #check for event
        if event.type == pygame.QUIT:   #if event is of type to quit, running = False
            running = False

        #stores key pressed
        keys = pygame.key.get_pressed() 
      
        # if left arrow key is pressed 
        if keys[pygame.K_LEFT] and rocketx>0: 
            
            # decrement in x co-ordinate 
            rocketx -= vel 
            
        # if right arrow key is pressed 
        if keys[pygame.K_RIGHT] and rocketx<360-50: 
            
            # increment in x co-ordinate 
            rocketx += vel 

    bullety = bullety + 1
    surface.fill((0,0,0))

    surface.blit(monster_img, (50,0))
    surface.blit(rocket_img, (rocketx,rockety))
    surface.blit(bullet_img, (bulletx, bullety)) 
    if rockety<(bullety+bulletsize):
        bullety = 720+1
        if (((rocketx<(bulletx+bulletsize))and ((rocketx+rocketsize)>(bulletx+bulletsize)))or (((rocketx+rocketsize)>bulletx)and((rocketx+rocketsize)<(bulletx+bulletsize)))or ((rocketx<(bulletx)) and ((rocketx+rocketsize)>(bulletx+bulletsize)))):
            rockethealth = rockethealth - 20
            healthbar = healthbar + 144
            Strike.play()

    pygame.draw.rect(surface, (255, 0, 0), [0, healthbar, 10, 720])
    
    if bullety>720:
        Shot.play()
        bullety = 150
        bulletx = random.randint(0, 360-bulletsize)
    
    if rockethealth<=0:
        End.play()
        pygame.time.wait(1000)
        running = False

    pygame.display.update()     #Update the GUI