import time
import RPi.GPIO as GPIO
import keyboard

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A = 7
B = 11
C = 13
D = 15
E = 32
F = 36
G = 38
H = 40

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(H, GPIO.OUT)

def GPIO_SETUP(a,b,c,d,e,f,g,h):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    GPIO.output(E, e)
    GPIO.output(F, f)
    GPIO.output(G, g)
    GPIO.output(H, h)
    time.sleep(0.001)

def MARCHE_ARRIERE(deg):
    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0,0,0,0,0)
    while degree > 0.0:
        GPIO_SETUP(1,0,0,0,1,0,0,1)
        GPIO_SETUP(1,1,0,0,0,0,0,1)
        GPIO_SETUP(0,1,0,0,0,0,1,1)
        GPIO_SETUP(0,1,1,0,0,0,1,0)
        GPIO_SETUP(0,0,1,0,0,1,1,0)
        GPIO_SETUP(0,0,1,1,0,1,0,0)
        GPIO_SETUP(0,0,0,1,1,1,0,0)
        GPIO_SETUP(1,0,0,1,1,0,0,0)
        degree -= 1

def MARCHE_AVANT(deg):
    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0,0,0,0,0)
    while degree > 0.0:
        GPIO_SETUP(1,0,0,1,1,0,0,0)
        GPIO_SETUP(0,0,0,1,1,1,0,0)
        GPIO_SETUP(0,0,1,1,0,1,0,0)
        GPIO_SETUP(0,0,1,0,0,1,1,0)
        GPIO_SETUP(0,1,1,0,0,0,1,0)
        GPIO_SETUP(0,1,0,0,0,0,1,1)
        GPIO_SETUP(1,1,0,0,0,0,0,1)
        GPIO_SETUP(1,0,0,0,1,0,0,1)
        degree -= 1

def TOURNER_GAUCHE(deg):
    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0,0,0,0,0)
    while degree > 0.0:
        GPIO_SETUP(1,0,0,0,1,0,0,0)
        GPIO_SETUP(1,1,0,0,1,1,0,0)
        GPIO_SETUP(0,1,0,0,0,1,0,0)
        GPIO_SETUP(0,1,1,0,0,1,1,0)
        GPIO_SETUP(0,0,1,0,0,0,1,0)
        GPIO_SETUP(0,0,1,1,0,0,1,1)
        GPIO_SETUP(0,0,0,1,0,0,0,1)
        GPIO_SETUP(1,0,0,1,1,0,0,1)
        degree -= 1

def TOURNER_DROITE(deg):
    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0,0,0,0,0)
    while degree > 0.0:
        GPIO_SETUP(1,0,0,1,1,0,0,1)
        GPIO_SETUP(0,0,0,1,0,0,0,1)
        GPIO_SETUP(0,0,1,1,0,0,1,1)
        GPIO_SETUP(0,0,1,0,0,0,1,0)
        GPIO_SETUP(0,1,1,0,0,1,1,0)
        GPIO_SETUP(0,1,0,0,0,1,0,0)
        GPIO_SETUP(1,1,0,0,1,1,0,0)
        GPIO_SETUP(1,0,0,0,1,0,0,0)
        degree -= 1

    GPIO_SETUP(0,0,0,0,0,0,0,0)
