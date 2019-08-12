# bin
bin des scripts relatifs à la raspberry Pi (moteurs, capteurs, etc...)

Le fichier start.py appel tous les autres scripts:
-	strl2Roues.py 	: avance, recule, gauche et droite de 2 roues latérales (moteurs pas à pas controlés par ULN2003)
-	captHC.py 	: mesure de la distance avec capteur HC-SR04 ultrasons
-	autoHC.py	: avance un peu, s'arrete, prend la distance, et reavance ... jusqu'à ce que distance < distance donnée de sécurité collision
-	reset.py	: Heu... Reset

![RaspberryPi4|20%](images/raspberry-pi-4.jpg "RaspberryPi4")
![Moteur_28byj-48_avec_ULN2003|100x100, 20%](images/28byj-48.png "Moteur_28byj-48_avec_ULN2003")
![HC-SR04_ultrasons|100x100](images/HC-SR04_100x100.jpg "HC-SR04_ultrasons")

* puis Bien des nouveaux scripts à venir...
