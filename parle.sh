#!/bin/bash
#

function Parle(){
	local parle="Hello $1 eoTO hip hop $1 h11ip haaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhahhahaahahha tuupuuduucuulaamoorooïïdee $1 op et et Yioiyupla"
	wget -q -U Mozilla -O output.mp3 "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q='$parle'&tl=Fr-fr"
	mplayer output.mp3
}

Parle
