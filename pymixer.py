# https://github.com/xavraspi/bin.git
# Usage: pymixer.Mixer()
import time, sys
import pygame

def Mixer(son):
    pygame.mixer.init()
    pygame.mixer.music.load(son)
    #pygame.mixer.Channel(2)
    pygame.mixer.music.play()
#    time.sleep(3) à utiliser pour entendre le son quand aucun process derriere.

#    volume = pygame.mixer.music.get_volume()

#Mixer('./sons/NO.mp3')

