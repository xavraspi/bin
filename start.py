#!/usr/bin/env python3
# https://github.com/xavraspi/bin.git
# Usage: Au clavier AZERTY z,s,q,d, y,n, m,t, r
import time
import keyboard
import sys, os
import pymixer
import captHC, autoHC, reset, bmp280, ctrl2Roues

path = "/home/pi/bin/start.py"
chemin = os.path.dirname(path)
theme = "thm_starwars/"

def Action(action):
        pymixer.Mixer("{}/sons/{}{}.mp3".format(chemin, theme, action))
        print(action)
   
while True:

   if keyboard.is_pressed('q'):
        Action('TOURNER_GAUCHE')
        ctrl2Roues.TOURNER_GAUCHE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('d'):
        Action('TOURNER_DROITE')
        ctrl2Roues.TOURNER_DROITE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('s'):
        Action('MARCHE_ARRIERE')
        ctrl2Roues.MARCHE_ARRIERE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('z'):
        Action('MARCHE_AVANT')
        ctrl2Roues.MARCHE_AVANT(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('n'): # NON
        Action('NO')
        ctrl2Roues.TOURNER_DROITE(6)
        ctrl2Roues.TOURNER_GAUCHE(6)
        ctrl2Roues.TOURNER_DROITE(6)
        ctrl2Roues.TOURNER_GAUCHE(6)
        ctrl2Roues.TOURNER_DROITE(12)
        ctrl2Roues.TOURNER_GAUCHE(12)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('y'): # YES 
        Action('YES')
        ctrl2Roues.MARCHE_AVANT(10)
        ctrl2Roues.MARCHE_ARRIERE(10)
        ctrl2Roues.MARCHE_AVANT(5)
        ctrl2Roues.MARCHE_ARRIERE(3)
        ctrl2Roues.MARCHE_AVANT(5)
        ctrl2Roues.MARCHE_ARRIERE(3)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('m'): # mesurer distance
        Action('MESURE')
        captHC.dist(1) 
   elif keyboard.is_pressed('t'):
        Action('TEMPRESSION')
        bmp280.bmp280()            
   elif keyboard.is_pressed('A'):
        Action('AUTO')
        autoHC.auto(15)            
   elif keyboard.is_pressed('space'):
        Action('meteo')
        time.sleep(1)
   elif keyboard.is_pressed('r'):
        Action('RESET')
        reset.reset(0)
        

