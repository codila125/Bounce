import pygame   #importing pygame library
pygame.init()   #initializing pygame

surface = pygame.display.set_mode((1080, 720), pygame.RESIZABLE)     #setting the size of the game window and also making it resizable

pygame.display.set_caption("Bounce")     #Setting the title of our game window
Icon = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Icon.png")      #Loading image first before setting it
pygame.display.set_icon(Icon)   #Setting an icon of the game window

vel = 10
x = 540
y = 670
rocket_img = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Rocket.png")
rocket_img = pygame.transform.scale(rocket_img,(50,50))

monster_img = pygame.image.load("/Users/prabesh/Documents/Github/Bounce/app_media/Space Monster.png")
monster_img = pygame.transform.scale(monster_img, (1000,200))

running = True
while running:  #keep game running till running is true

    for event in pygame.event.get():    #check for event
        if event.type == pygame.QUIT:   #if event is of type to quit, running = False
            running = False

        #stores key pressed
        keys = pygame.key.get_pressed() 
      
        # if left arrow key is pressed 
        if keys[pygame.K_LEFT] and x>50: 
            
            # decrement in x co-ordinate 
            x -= vel 
            
        # if right arrow key is pressed 
        if keys[pygame.K_RIGHT] and x<1080-50: 
            
            # increment in x co-ordinate 
            x += vel 

    surface.fill((0,0,0))

    surface.blit(monster_img, (50,-50))
    surface.blit(rocket_img, (x,y))
    
    pygame.display.update()     #Update the GUI