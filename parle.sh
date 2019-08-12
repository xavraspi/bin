#!/bin/bash
#
python start.py

Parle ()
{
	parle=$(echo "Gooodailleniooos")
	wget -q -U Mozilla -O output.mp3 "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q='RREUH HIHICHICHICHITITITOTITO $parle GONEZALESSE et et'&tl=Fr-fr"
	mplayer output.mp3
}

Parle

