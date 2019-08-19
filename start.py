# https://github.com/xavraspi/bin.git
# Usage: Au clavier AZERTY z,s,q,d, y,n, m,t, r
import time
import keyboard
import sys
import ctrl2Roues 
import pymixer
import captHC

#sys.path.append('/media/pi/COPYX/bin')

while True:

   if keyboard.is_pressed('q'):
        pymixer.Mixer('./sons/TOURNER_GAUCHE.mp3')
        print('GAUCHE')
        ctrl2Roues.TOURNER_GAUCHE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('d'):
        pymixer.Mixer('./sons/TOURNER_DROITE.mp3')
        print('DROITE')
        ctrl2Roues.TOURNER_DROITE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('s'):
        pymixer.Mixer('./sons/MARCHE_ARRIERE.mp3')
        print('RECULER')
        ctrl2Roues.MARCHE_ARRIERE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('z'):
        pymixer.Mixer('./sons/MARCHE_AVANT.mp3')
        print('AVANCER')
        ctrl2Roues.MARCHE_AVANT(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('n'): # NON
        print('NO!')
        pymixer.Mixer('./sons/NO.mp3')
        ctrl2Roues.TOURNER_DROITE(6)
        ctrl2Roues.TOURNER_GAUCHE(6)
        ctrl2Roues.TOURNER_DROITE(6)
        ctrl2Roues.TOURNER_GAUCHE(6)
        ctrl2Roues.TOURNER_DROITE(12)
        ctrl2Roues.TOURNER_GAUCHE(12)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('y'): # YES 
        print('YES!')
        pymixer.Mixer('./sons/YES.mp3')
        ctrl2Roues.MARCHE_AVANT(10)
        ctrl2Roues.MARCHE_ARRIERE(10)
        ctrl2Roues.MARCHE_AVANT(5)
        ctrl2Roues.MARCHE_ARRIERE(3)
        ctrl2Roues.MARCHE_AVANT(5)
        ctrl2Roues.MARCHE_ARRIERE(3)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
   elif keyboard.is_pressed('m'): # mesurer distance
        pymixer.Mixer('./sons/MESURE.mp3')
        print('MESURE')
        captHC.dist(1) 
   elif keyboard.is_pressed('t'):
        print('AUTO')
        pymixer.Mixer('./sons/output.mp3')
        import autoHC 
        autoHC.auto(15)            
   elif keyboard.is_pressed('r'):
        print('RESET')
        pymixer.Mixer('./sons/RESET.mp3')
        import reset
        reset.reset(0)
        

