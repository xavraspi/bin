# https://github.com/xavraspi/bin.git
# Usage: autoHC.auto(Limite_collision)

import RPi.GPIO as GPIO
import time
import ctrl2Roues


distance = 33
limite = 3 

def auto(limite = "10"):

   global distance
#   global limite
#   GPIO.setmode(GPIO.BCM)
   GPIO.setmode(GPIO.BOARD)
   GPIO.setwarnings(False)
#print "+-----------------------------------------------------------+"
#print "|   Mesure de distance par le capteur ultrasons HC-SR04   |"
#print "+-----------------------------------------------------------+"



   Trig = 16          # Entree Trig du HC-SR04
   Echo = 18          # Sortie Echo du HC-SR04

   GPIO.setup(Trig,GPIO.OUT)
   GPIO.setup(Echo,GPIO.IN)

   GPIO.output(Trig, False)

   while float(limite) < float(distance):
       print (distance)
       ctrl2Roues.MARCHE_AVANT(100)
       ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)

       time.sleep(0.2)       # histoire de ...
       GPIO.output(Trig, True)
       time.sleep(0.00001)
       GPIO.output(Trig, False)

       while GPIO.input(Echo)==0:  ## Emission de l'ultrason Trig
         debutImpulsion = time.time()

       while GPIO.input(Echo)==1:   ## Retour de l'Echo
         finImpulsion = time.time()

       distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
       GPIO.output(Trig, False)
   

   else:
       print ("COLLISION MUR",limite,".",distance)
       ctrl2Roues.TOURNER_DROITE(25)
       ctrl2Roues.TOURNER_GAUCHE(25)
       ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)
       distance = limite + 1

#auto(20)
