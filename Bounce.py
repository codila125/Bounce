import pygame   #importing pygame library  
pygame.init()   #initializing pygame

surface = pygame.display.set_mode((1080, 720), pygame.RESIZABLE)     #setting the size of the game window and also making it resizable

pygame.display.set_caption("Bounce")     #Setting the title of our game window
Icon = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Icon.png")      #Loading image first before setting it
pygame.display.set_icon(Icon)   #Setting an icon of the game window


running = True
while running:  #keep game running till running is true

    for event in pygame.event.get():    #check for event
        if event.type == pygame.QUIT:   #if event is of type to quit, running = False
            running = False

    pygame.draw.circle(surface, (250,250,250), (540,360), 10)     #Draw circle
    
    pygame.display.update()     #Update the GUI