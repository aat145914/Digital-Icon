#Renamed repository Digital-Icon

import os
from datetime import date
from time import sleep

#Check if folder contains a ver2.py (meaning updated ver) and rename ver.py, new ver 14
filelist1 = [ f for f in os.listdir('/home/pi/icons') if (f.endswith('ver2.py'))]
if filelist1:
	#remove old ver.py
	filelist2 = [ f for f in os.listdir('/home/pi/icons') if (f.endswith('ver.py'))]
	for f in filelist2:
		os.remove('/home/pi/icons/'+f) 
	#rename ver2.py to ver.py
	if filelist2:
		os.system('sudo mv ' +'/home/pi/icons/ver2.py '+ '/home/pi/icons/ver.py')

#Figure out current date
today = date.today()
day = today.day			#testing
month = today.month

#Check tft resolution
pi_folder = '/home/pi/'

workfile1 = pi_folder + 'tft.txt'
f = open(workfile1, 'r')

current_tft_res = []

for i in f: 
	i = i.strip('\n')
	current_tft_res.append(i)

s = ''.join(map(str,current_tft_res))
current_tft_res = str(s)
print("Let's see tft res")
print(current_tft_res)

#Determine version
workfile1 = pi_folder + 'ver.txt'
f = open(workfile1, 'r')	

current_ver_num = []

for i in f: 
	i = i.strip('\n')
	current_ver_num.append(i)

s = ''.join(map(str,current_ver_num))
current_ver_num = int(s)
print("Let's see version number")
print(current_ver_num)
#end versioning

import sys
sys.path.append('/home/pi')
#Check if in Easter season
from Easter import Eastercheck 
Chk = Eastercheck()
#If are in Easter season, replace spaces with dash
if Chk:
	Chk = Chk.replace(" ", "-")

#print(Chk)
#day = 26				#testing
#month = 2

#Remove all icons from last start
filelist = [ f for f in os.listdir('/home/pi/icons') if (f.endswith('.jpg') or f.endswith('.txt'))]
for f in filelist:
	os.remove('/home/pi/icons/'+f)

#Proceed if in Easter season	
if Chk:					
	print(Chk)

	os.system('curl -o ' + '/home/pi/icons/'+Chk + '.txt ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res + '/' + 'Easter' + '/' + Chk + '.txt') 
	
	sleep(5)		#ver 11
	workfile = '/home/pi/icons/' + Chk + '.txt'
	f = open(workfile, 'r')

	files = []
	
	for i in f:
		if (Chk in i):
			i = i.strip('\n')
			files.append(i)
			
	print(files)
	count = 0
	#Count number of Easter feast .jpgs to d/l
	for file in files:
		count+=1
		print(file)		
		
	filename = Chk + '_'
	j = 1
	#D/l Easter feast icons
	while j <= count:
		os.system('curl -o ' + '/home/pi/icons/'+ filename + str(j) + '.jpg ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res +'/' +'Easter' + '/' + filename + str(j) + '.jpg') 
		if j == count:
			break
		j+=1	

#Add zero to days & months <10		
if day<10:
	day = str(day)
	day = "0" + day
if month<10:
	month = str(month)
	month = "0" + month

day = str(day)
month = str(month)	

partfile = month + day

#D/l days' icons.txt
os.system('curl -o ' + '/home/pi/icons/'+partfile + '.txt ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res + '/' + month + '/' + partfile + '.txt') 

sleep(5)			#ver 11
	
workfile = '/home/pi/icons/' + month + day + '.txt'
f = open(workfile, 'r')
	
files = []

for i in f: 
    if (partfile in i):
        i = i.strip('\n')
        files.append(i)

print(files)
count = 0
#Count number of days' icons
for file in files:
	count+=1
	print(file)

filename = partfile + '_'
j = 1
#D/l days icons according to tft res.
while j <= count:
	os.system('curl -o ' + '/home/pi/icons/'+ filename + str(j) + '.jpg ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res +'/' + month + '/' + filename + str(j) + '.jpg') 
	if j == count:
		break
	j+=1	

#Call Display_v(current_ver_num)	
file = '/home/pi/Display_v' + str(current_ver_num) + '.py'
os.system('sudo python ' + str(file))    

