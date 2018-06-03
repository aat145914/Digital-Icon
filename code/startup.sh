#!/bin/bash
# My first script

x=0
proceed=0
#for i in 0;  #for i in 0 1; 
while [ $x -le 100 ]
do
	if [  "$(ping -c 1 8.8.8.8)" ]; then
		echo Network connected
		proceed=1
		break
	fi
	sleep 0.1
	x=$(( $x+1 ))
done


#do
#	if !  [  "$(ping -c 1 8.8.8.8)" ]; then
#		sudo ifdown wlan0
#		sleep 4
#		sudo ifup wlan0
#		sleep 12 #instead of 15 #30 worked 
#		echo Network problems
#	else
#		echo Network connected
#		proceed=1
#	fi
#done

#works#proceed=1
#echo The counter is $i

#works#if [ $proceed -eq 0 ]; then
if [ $proceed -eq 1 ]; then
	#return
	#sudo python example4.py
	cd /
	#cd home/pi/				#working but old ver.
	#sudo python example5.py	#working but old ver.
	cd home/pi/icons/
	
	sudo python ver.py 	#testing#readingfromfilelnx.py
	#echo here
	cd /
else
	#echo there
	sudo startx
fi

#cd /
#cd home/pi/bin
#sudo python example4.py
#cd /
