import RPi.GPIO as GPIO
import ctrl2Roues
import time
ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)

def reset(etat):
   ctrl2Roues.GPIO_SETUP(0,0,0,1,0,0,0,1)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(0,0,1,0,0,0,1,0)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(0,1,0,0,0,1,0,0)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(1,0,0,0,1,0,0,0)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(0,1,0,0,0,1,0,0)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(0,0,1,0,0,0,1,0)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(0,0,0,1,0,0,0,1)
   time.sleep(0.2)

   ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)

   distance = ""
   limite = ""
   debutImpulsion = ""
   finImpulsion = ""

   ctrl2Roues.GPIO_SETUP(0,1,0,1,0,1,0,1)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(1,0,1,0,1,0,1,0)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(1,0,0,1,1,0,0,1)
   time.sleep(0.2)
   ctrl2Roues.GPIO_SETUP(0,1,1,0,0,1,1,0)
   time.sleep(0.2)

   ctrl2Roues.GPIO_SETUP(0,0,0,0,0,0,0,0)


#GPIO.cleanup
#exit(1)
