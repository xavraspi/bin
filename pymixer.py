# https://github.com/xavraspi/bin.git
# Usage: pymixer.Mixer()
import time, sys
import pygame

def Mixer(son):
    pygame.mixer.init()
    pygame.mixer.music.load(son)
    #pygame.mixer.Channel(2)
    pygame.mixer.music.play()
#    time.sleep(3)

#    volume = pygame.mixer.music.get_volume()
#    print ("Son est Playing : ", isplaying, ", Volume: ", volume)
#    exit(0)
#print("done")

#Mixer('./sons/NO.mp3')

