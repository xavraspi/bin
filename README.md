# bin
bin des scripts relatifs à la raspberry Pi (moteurs, capteurs, etc...)

![RaspberryPi4](images/raspberry-pi-4.jpg "RaspberryPi4")

Le fichier start.py appel tous les autres scripts:
-	strl2Roues.py 	: avance, recule, gauche et droite de 2 roues latérales (moteurs pas à pas controlés par ULN2003)
![Moteur_28byj-48_avec_ULN2003](images/28byj-48.png "Moteur_28byj-48_avec_ULN2003")
-	captHC.py 	: mesure de la distance avec capteur HC-SR04 ultrasons
-	autoHC.py	: avance un peu, s'arrete, prend la distance, et reavance ... jusqu'à ce que distance < distance donnée de sécurité collision

![HC-SR04_ultrasons](images/HC-SR04_100x100.jpg "HC-SR04_ultrasons")

- pymixer.py :  lecture d'un sample lors de l'appele d'une commande 
                Usage: pymixer.Mixer('output.mp3')

- bmp280.py : capteur de temperature, pression (et humidité...)

![bme-bmp280_GYBMEP](images/bme-bmb280_GYBMEP.jpeg "bme-bmp280_GYBMEP")

-	reset.py	: Heu... Reset


