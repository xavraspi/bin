#import time
#import RPi.GPIO as GPIO
import keyboard
import sys
from sh import parle

sys.path.append('/media/pi/COPYX/bin')
import ctrl2Roues 
# Usage: ctrl2Roues.MARCHE_AVANT(degrees)
# 2 roues ULN2003 Pin roue_gauche 7,11,13,15 ; roue_droite 32,36,38,40

# sys.path.append('/home/pi/bin/python/HC-SR04')


while True:

   if keyboard.is_pressed('q'):
        print('GAUCHE')
        ctrl2Roues.TOURNER_GAUCHE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('e'): # parle.sh
        print('Parle')
        
#        from sh import parle
#        print sh.ifconfig("wlan0")
   elif keyboard.is_pressed('d'):
        print('DROITE')
        ctrl2Roues.TOURNER_DROITE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('s'):
        print('RECULER')
        ctrl2Roues.MARCHE_ARRIERE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('z'):
        print('AVANCER')
        ctrl2Roues.MARCHE_AVANT(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('n'): # NON
        print('NO!')
        ctrl2Roues.TOURNER_DROITE(6)
        ctrl2Roues.TOURNER_GAUCHE(6)
        ctrl2Roues.TOURNER_DROITE(6)
        ctrl2Roues.TOURNER_GAUCHE(6)
        ctrl2Roues.TOURNER_DROITE(12)
        ctrl2Roues.TOURNER_GAUCHE(12)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('y'): # YES 
        print('YES!')
        ctrl2Roues.MARCHE_AVANT(10)
        ctrl2Roues.MARCHE_ARRIERE(10)
        ctrl2Roues.MARCHE_AVANT(5)
        ctrl2Roues.MARCHE_ARRIERE(3)
        ctrl2Roues.MARCHE_AVANT(5)
        ctrl2Roues.MARCHE_ARRIERE(3)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('m'): # mesurer distance
        print('MESURE')
        import captHC 
# Usage: captHC.dist(Nbre_mesures)
# Pin Trig 16 ; Echo 18
#        captHC.dist(1)
#        from captHC import limite
#        print("WARNING %s" % str(limite))
   elif keyboard.is_pressed('t'):
        print('AUTO')
        import autoHC 
        autoHC.auto(15)            
   elif keyboard.is_pressed('r'):
        print('RESET')
        import reset
        reset.reset(0)
        

