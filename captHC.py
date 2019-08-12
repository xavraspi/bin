import RPi.GPIO as GPIO
import time

def dist(nbre):

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

   debutImpulsion = "0"
   finImpulsion = "0"

   time.sleep(0.1)       # histoire de ...

   GPIO.output(Trig, True)
   time.sleep(0.00001)
   GPIO.output(Trig, False)
   
   while GPIO.input(Echo)==0:  ## Emission de l'ultrason Trig
     debutImpulsion = time.time()

   while GPIO.input(Echo)==1:   ## Retour de l'Echo
     finImpulsion = time.time()

   distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
   distance = str(distance)
   Nbre = len(distance)
   if Nbre > 4:
       print ("Distance :",distance[:1],"m et",distance[1:],"cm")
   else:
       print ("Distance :",distance,"cm")

   GPIO.output(Trig, False)
#GPIO.cleanup()
#exit(0)
#dist(1)

