# bin
bin des scripts relatifs à la raspberry Pi (moteurs, capteurs, etc...)

Le fichier start.py appel tous les autres scripts:
-	strl2Roues.py 	: avance, recule, gauche et droite de 2 roues latérales (moteurs pas à pas controlés par ULN2003)
-	captHC.py 	: mesure de la distance avec capteur HC-SR04 ultrasons
-	autoHC.py	: avance un peu, s'arrete, prend la distance, et reavance ... jusqu'à ce que distance < distance donnée de sécurité collision
-	reset.py	: Heu... Reset

![RaspberryPi4](https://images.frandroid.com/wp-content/uploads/2019/06/raspberry-pi-4-1200x857.jpg?width=100 "RaspberryPi4")
![Moteur_28byj-48_avec_ULN2003](https://market.samm.com/28byj-48-stepper-motor-uln2003-driver-card-general-in-428-25-O.png?width=50 "Moteur_28byj-48_avec_ULN2003")
![HC-SR04_ultrasons](https://images.amain.com/images/large/ose/osehc-sr04.jpg?s=100?width=50 "HC-SR04_ultrasons")

* puis Bien des nouveaux scripts à venir...
