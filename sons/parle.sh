#!/bin/bash
#
date=`date -u`

function Parle(){
	local parle="Hello $1 eoTO hip hop $1 h11ip haaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhahhahaahahha tuupuuduucuulaamoorooïïdee $1 op et et Yioiyupla"
	wget -q -U Mozilla -O output.mp3 "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q='$parle'&tl=Fr-fr"
#	mplayer output.mp3
}


function Meteo(){
	meteo=`curl http://www.prevision-meteo.ch/services/json/$1`
#	meteo=`curl http://www.prevision-meteo.ch/services/json/[ville]`
	ville=$(echo $meteo | jq ".city_info.name")
	condition=$(echo $meteo | jq ".current_condition.condition")
	tempactu=$(echo $meteo | jq ".current_condition.tmp")
	tempmin=$(echo $meteo | jq ".fcst_day_0.tmin")
	tempmax=$(echo $meteo | jq ".fcst_day_0.tmax")
	local parle1="Aujourd'hui $date à $ville $condition avec des températures de $tempmin à $tempmax degrés. Là, Il fait $tempactu degrées."
	wget -q -U Mozilla -O meteo.mp3 "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q='$parle1'&tl=Fr-fr"
#	mplayer meteo.mp3
	echo -e "$date\n$ville\n$condition\n$tempactu\n$tempmin\n$tempmax\n$parle1" > ../meteo.txt
}

#Parle
Meteo cuers

