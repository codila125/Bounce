import pygame   #importing pygame library
pygame.init()   #initializing pygame

from pygame import mixer    #importing mixer which is used for audio works
mixer.init()    #initializing mixer
Strike = mixer.Sound("Space-Cowboy/app_media/Strike.mp3")   #loading required audio files
Shot = mixer.Sound("Space-Cowboy/app_media/Shot.mp3")
Loss = mixer.Sound("Space-Cowboy/app_media/Loss.mp3")
Win = mixer.Sound("Space-Cowboy/app_media/Win.mp3")

import random   #importing random for random no. generation

surface = pygame.display.set_mode((360, 720))     #setting the size of the game window

pygame.display.set_caption("Space Cowboy")     #Setting the title of our game window
Icon = pygame.image.load("Space-Cowboy/app_media/Icon.png")      #Loading image first before setting it
pygame.display.set_icon(Icon)   #Setting an icon of the game window

bg_img = pygame.image.load("Space-Cowboy/app_media/Background.jpeg")  #loading background image  

#dimensions required for rocket
rocketsize = 60
vel = 20
rocketx = 180
rockety = 670
rockethealth = 500
healthbar = 0
rocket_img = pygame.image.load("Space-Cowboy/app_media/rocket.png")
rocket_img = pygame.transform.scale(rocket_img,(rocketsize,rocketsize))

#dimensions required for mafia
mafiahealth = 2000
mafiabar = 0
mafia_img = pygame.image.load("Space-Cowboy/app_media/Space Mafia.png")
mafia_img = pygame.transform.scale(mafia_img, (250,170))

#dimensions of lazer
lasersize = 40
laserx = random.randint(0, 360-lasersize)       #randomly generating numbers from given range
lasery = 100
laser_img = pygame.image.load("Space-Cowboy/app_media/Laser.png")
laser_img = pygame.transform.scale(laser_img, (lasersize,lasersize))

#dimension of rasengan
lightsize = 30
lightx = rocketx
lighty = rockety
light_img = pygame.image.load("Space-Cowboy/app_media/Rasengan.png")
light_img = pygame.transform.scale(light_img, (lightsize,lightsize))

running = True
while running:  #keep game running till running is true

    surface.blit(bg_img, (0,0))     #running background image in the surface

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

    lighty = lighty - 1     #speed of ransengan by rocket
    lasery = lasery + 1.5        #speed of lazer by mafia

    surface.blit(mafia_img, (50,0))     #putting ufo on top
    surface.blit(rocket_img, (rocketx,rockety))     #putting our rocket in the bottom
    surface.blit(laser_img, (laserx, lasery))       #putting lasers on surface
    surface.blit(light_img, (lightx, lighty))       #putting rasengan on surface

    if rockety<(lasery+lasersize):  #finding out if the laser hits rocket
        lasery = 720+1      #moving the laser image down the surface so that it can be resent from top
        if (((rocketx<(laserx+lasersize))and ((rocketx+rocketsize)>(laserx+lasersize)))or (((rocketx+rocketsize)>laserx)and((rocketx+rocketsize)<(laserx+lasersize)))or ((rocketx<(laserx)) and ((rocketx+rocketsize)>(laserx+lasersize)))):
            rockethealth = rockethealth - 50        #if the laser hits, health of rocket is decreased
            healthbar = healthbar + 72      #healthbar shows is
            Strike.play()   #well some sounds for proof

    pygame.draw.rect(surface, (0, 0, 255), [0, healthbar, 10, 720])     # constantly refreshing the health bar according to health

    if lasery>720:      #if the laser is already out of our surface, recyclying it
        Shot.play()     #since couldnot play it when it shoots, played it when it reaches the bottom
        lasery = 100
        laserx = random.randint(0, 360-lasersize)       
    
    if lighty <= 100:       #if the rasengan has already hit the mafia, recycling it
        lighty = rockety        #starting again from rocket
        lightx = rocketx
        mafiahealth = mafiahealth - 50      #health deacreases when rasengan hits
        mafiabar = mafiabar + 18        #shown by mafiabar
    
    pygame.draw.rect(surface, (255, 0, 0), [350, mafiabar, 360, 720])       #contantly refreshing mafiabar
    
    if rockethealth <= 0:   #if we lose, game ends
        Loss.play()     #playing losing music
        pygame.time.wait(1000)      #waiting for music to finish
        running = False

    if mafiahealth<=0:      #game ends even when we win
        Win.play()      #playing winner music
        pygame.time.wait(3000)      #waiting untill the winner music finishes
        running = False

    pygame.display.update()     #Update the GUI constantly