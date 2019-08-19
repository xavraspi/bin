# https://github.com/xavraspi/bin.git
# Usage: Au clavier AZERTY z,s,q,d, y,n, m,t, r
import time
import keyboard
import sys
import ctrl2Roues 

#sys.path.append('/media/pi/COPYX/bin')

while True:

   if keyboard.is_pressed('q'):
        print('GAUCHE')
        ctrl2Roues.TOURNER_GAUCHE(20)
        ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
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
        

