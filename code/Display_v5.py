# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#ver 6: added daycounter that checks day so that changes if left on and passes midnight
#ver4 (git)
#ver5 (git)  update Easter to take variables
#for Testing: manual change date in 2 places

from time import sleep

import sys
import os
from datetime import date

import RPi.GPIO as GPIO2

#New to v5
import subprocess
subprocess.Popen(["python", "/home/pi/icons/subproc_test_v5.py"])

GPIO2.setmode(GPIO2.BCM)
backlight_pin = 18
pause_time = 0.02

GPIO2.setup(backlight_pin, GPIO2.OUT)
backlight = GPIO2.PWM(backlight_pin, 100)
backlight.start(100)

# Raspberry Pi configuration.
DC = 25  		#18 is for PWM
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Load an image.
print('Loading image...')

from pitftgpio import PiTFT_GPIO

pitft = PiTFT_GPIO()
today = date.today()

day = today.day			#testing
month = today.month
#-------------------------------------------------TESTING-------------------------------------------------------------#
#day = 4			
#month = 6				
#-------------------------------------------------TESTING-------------------------------------------------------------#

#Figure out day at start of icon initialization
#TESTING 
dayatstart = day
#dayatstart = 17

from Easter import Eastercheck		#Mod'd for ver change
Chk = Eastercheck(0,0,0)

from Saints import months
#get January, Febuary etc. from array
month_of_year = months[month-1]	

if Chk:
	Chk = Chk.replace(" ", "-")

if day<10:
	day = "0" + str(day)
if month<10:
	month = "0" + str(month)
day = str(day)
str_month_day = month + day #"0117"

#print(str_month_day)
tuple_of_day = month_of_year[str_month_day]
#print(tuple_of_day)

#Need this to make dictionary of saints:#oficons
no_of_saints = {}
saint = 1
for num in tuple_of_day:
	no_of_saints.update({saint:num})
	saint += 1

def fadeIn():						#Not used
	for i in range(10,101):      	#101 because it stops when it finishes 100
		backlight.ChangeDutyCycle(i)
		sleep(pause_time)

def fadeOut():						#Not used
	backlight.ChangeDutyCycle(4)

def restart():						#Not used
	os.system("sudo reboot")

def Easterloop(eastericon):
	imagenum = 0					#changed from 1 to 0, ver4
	iconimg=''
	#Find and load first Easter feast image
	iconimg = '/home/pi/icons/' + eastericon + '_' + str(imagenum) + ".jpg"
	os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose ' + iconimg)
	imagenum += 1
	iconimg = '/home/pi/icons/' + eastericon + '_' + str(imagenum) + ".jpg"
	#Check if second Easter feast image exists
	firstcheck = os.path.isfile(iconimg)
	count = 0
	#If second image exists enter
	if firstcheck:					
		imagenum = 0				#changed from 1 to 0, ver4
		while True:		
		
			sleep(0.25)
			count += 0.25
			if count == 15.0:
				imagenum += 1
				#print("Do something here")
				count = 0
				print('Loading image...')
				iconimg=''
				iconimg = '/home/pi/icons/' + eastericon + '_' + str(imagenum) + ".jpg"
				#Keep checking if subsequent images exits
				check = os.path.isfile(iconimg)
				#If exists show
				if check:
					os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose ' + iconimg)
				#Otherwise break
				else:		
					break
			#Keep fuctionality of buttons during loop
			if pitft.Button1:
				print "Button 1 pressed - screen off"
				os.system('sudo startx')
			if pitft.Button2:
				print "Button 2 pressed - screen on"
				os.system('sudo startx -- -layout HDMI')
			if pitft.Button3:
				print "Button 3 pressed"
				os.system('sudo startx -- -layout HDMI')
			if pitft.Button4:
				print "Button 4 pressed"
				os.system('sudo startx -- -layout HDMI')
		#Return from break, no more images
		return
	
	#If no second image wait for 15 secons then return	
	else:
		while True:
			sleep(0.25)
			count += 0.25
			if count == 15.0:
				break
		return

		
	
		
#Show day's icons first		
imagenum = 0					#changed from 1 to 0, ver4
		
count = 0
daycounter = 0
#imagenum = 0 			#changed from 1 to 0, ver4
#if firstcheck:

while True:
	if Chk:
		Easterloop(Chk)
	 
	for saint_no, icons in no_of_saints.items():
		number_of_icons = 0
		iconimg=''
		iconimg = '/home/pi/icons/' + month + day + '_0' + str(saint_no) + '_0' + str(number_of_icons) + '.jpg'
		os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose ' + iconimg)

		count=0
		sleep(0.25)
		while (True):
			
			sleep(0.25)
			count += 0.25
			daycounter += 0.25
			
			if (count == 15.0) :
				
				number_of_icons = int(number_of_icons) + 1
				if(number_of_icons == (icons+1)):
					count=0
					break
				if number_of_icons<10:
					number_of_icons = "0"+str(number_of_icons)
				else:
					number_of_icons = str(number_of_icons)
				
				print(number_of_icons)
				count = 0
				print('Loading image...')
				
				iconimg = '/home/pi/icons/' + month + day + '_0' + str(saint_no) + '_' + str(number_of_icons) + '.jpg'

				os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose ' + iconimg)
	
			if pitft.Button1:
				print "Button 1 pressed - screen off"
				os.system('sudo startx')
			if pitft.Button2:
				print "Button 2 pressed - screen on"
				os.system('sudo startx -- -layout HDMI')
			if pitft.Button3:
				print "Button 3 pressed"
				os.system('sudo startx -- -layout HDMI')
			if pitft.Button4:
				print "Button 4 pressed"
				os.system('sudo startx -- -layout HDMI')
			if (daycounter > 30):
#------------------------------------------------------------TESTING-------------------------------------------------#
				today = date.today()		#comment out next 4 lines for Easter check
				day2 = today.day
				#day2 = 4
#------------------------------------------------------------TESTING--------------------------------------------------#
				if (day2 != dayatstart):
					break
				daycounter = 0

#new versioning, need for recalling readingfromfilelnx_v
pi_folder = '/home/pi/'
workfile1 = pi_folder + 'ver.txt'
f = open(workfile1, 'r')	

current_ver_num = []

for i in f: 
	i = i.strip('\n')
	current_ver_num.append(i)

s = ''.join(map(str,current_ver_num))
current_ver_num = int(s) 
os.system('sudo python /home/pi/icons/readingfromfilelnx_v' + str(current_ver_num) + '.py')		#from break for changing day			