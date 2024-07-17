import pygame   #importing pygame library
pygame.init()   #initializing pygame

from pygame import mixer
mixer.init()
Strike = mixer.Sound("Space Cowboy/app_media/Strike.wav")
Shot = mixer.Sound("Space Cowboy/app_media/Shot.wav")
Loss = mixer.Sound("Space Cowboy/app_media/Loss.wav")
Win = mixer.Sound("Space Cowboy/app_media/Win.wav")

import random

surface = pygame.display.set_mode((360, 720))     #setting the size of the game window and also making it resizable

pygame.display.set_caption("Space Cowboy")     #Setting the title of our game window
Icon = pygame.image.load("Space Cowboy/app_media/Icon.png")      #Loading image first before setting it
pygame.display.set_icon(Icon)   #Setting an icon of the game window

bg_img = pygame.image.load("Space Cowboy/app_media/Background.jpeg")

rocketsize = 60
vel = 20
rocketx = 180
rockety = 670
rockethealth = 500
healthbar = 0
rocket_img = pygame.image.load("Space Cowboy/app_media/rocket.png")
rocket_img = pygame.transform.scale(rocket_img,(rocketsize,rocketsize))

mafiahealth = 2000
mafiabar = 0
mafia_img = pygame.image.load("Space Cowboy/app_media/Space Mafia.png")
mafia_img = pygame.transform.scale(mafia_img, (250,170))

lasersize = 40
laserx = random.randint(0, 360-lasersize)
lasery = 100
laser_img = pygame.image.load("Space Cowboy/app_media/Laser.png")
laser_img = pygame.transform.scale(laser_img, (lasersize,lasersize))

lightsize = 30
lightx = rocketx
lighty = rockety
light_img = pygame.image.load("Space Cowboy/app_media/Rasengan.png")
light_img = pygame.transform.scale(light_img, (lightsize,lightsize))

running = True
while running:  #keep game running till running is true

    surface.blit(bg_img, (0,0))

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

    lighty = lighty - 1
    lasery = lasery + 1

    surface.blit(mafia_img, (50,0))
    surface.blit(rocket_img, (rocketx,rockety))
    surface.blit(laser_img, (laserx, lasery)) 
    surface.blit(light_img, (lightx, lighty))

    if rockety<(lasery+lasersize):
        lasery = 720+1
        if (((rocketx<(laserx+lasersize))and ((rocketx+rocketsize)>(laserx+lasersize)))or (((rocketx+rocketsize)>laserx)and((rocketx+rocketsize)<(laserx+lasersize)))or ((rocketx<(laserx)) and ((rocketx+rocketsize)>(laserx+lasersize)))):
            rockethealth = rockethealth - 50
            healthbar = healthbar + 72
            Strike.play()

    pygame.draw.rect(surface, (0, 0, 255), [0, healthbar, 10, 720])

    if lasery>720:
        Shot.play()
        lasery = 100
        laserx = random.randint(0, 360-lasersize)
    
    if lighty <= 100:
        lighty = rockety
        lightx = rocketx
        mafiahealth = mafiahealth - 50
        mafiabar = mafiabar + 18
    
    pygame.draw.rect(surface, (255, 0, 0), [350, mafiabar, 360, 720])
    
    if rockethealth <= 0:
        Loss.play()
        pygame.time.wait(1000)
        running = False

    if mafiahealth<=0:
        Win.play()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()     #Update the GUI