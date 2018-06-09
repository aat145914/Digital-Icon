#!/bin/bash

x=0
proceed=0
 
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


if [ $proceed -eq 1 ]; then

	#1st fix for clock syncing
	#sudo service ntp stop
	#sudo ntpdate -s time.nist.gov
	#sudo service ntp start

	#2nd fix for clock syncing
	sudo dpkg-reconfigure ntp

	cd /

	cd home/pi/icons/
	
	sudo python ver.py 	

	cd /
else
	
	sudo startx
fi


