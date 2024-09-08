from pygame import mixer    #importing mixer which is used for audio works

mixer.init()    #initializing mixer

Strike = mixer.Sound("Space Cowboy/app_media/Strike.mp3")   #loading required audio files
Shot = mixer.Sound("Space Cowboy/app_media/Shot.mp3")
Loss = mixer.Sound("Space Cowboy/app_media/Loss.mp3")
Win = mixer.Sound("Space Cowboy/app_media/Win.mp3")