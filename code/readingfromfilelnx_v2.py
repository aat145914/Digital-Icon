import os
from datetime import date
from time import sleep

today = date.today()
day = today.day			#testing
month = today.month

#new versioning
pi_folder = '/home/pi/'

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
from Easter import Eastercheck 
Chk = Eastercheck()
if Chk:
	Chk = Chk.replace(" ", "-")

#print(Chk)
#day = 26				#testing
#month = 2

filelist = [ f for f in os.listdir('/home/pi/icons') if (f.endswith('.jpg') or f.endswith('.txt'))]
for f in filelist:
	os.remove('/home/pi/icons/'+f)

if Chk:					#Check if in Easter season
	print(Chk)
	#Chk = Chk.replace(" ", "%%20")
	#g = Chk
	
	#os.system('curl -o ' + '/home/pi/icons/'+ Chk + '.txt' + 'https://raw.githubusercontent.com/aat145914/Test/master/Easter/' + Chk + '.txt')
	os.system('curl -o ' + '/home/pi/icons/'+Chk + '.txt ' + 'https://raw.githubusercontent.com/aat145914/Test/master/' + 'Easter' + '/' + Chk + '.txt') 
	
	sleep(5)		#change ver11 from 10
	workfile = '/home/pi/icons/' + Chk + '.txt'
	f = open(workfile, 'r')
	
	#sleep(10)
	files = []
	
	for i in f:
		if (Chk in i):
			i = i.strip('\n')
			files.append(i)
			
	print(files)
	count = 0
	for file in files:
		count+=1
		print(file)		
		
	filename = Chk + '_'
	j = 1
	while j <= count:
		os.system('curl -o ' + '/home/pi/icons/'+ filename + str(j) + '.jpg ' + 'https://raw.githubusercontent.com/aat145914/Test/master/Easter' + '/' + filename + str(j) + '.jpg') 
		if j == count:
			break
		j+=1	
		
if day<10:
	day = str(day)
	day = "0" + day
if month<10:
	month = str(month)
	month = "0" + month

day = str(day)
month = str(month)	

partfile = month + day

os.system('curl -o ' + '/home/pi/icons/'+partfile + '.txt ' + 'https://raw.githubusercontent.com/aat145914/Test/master/' + month + '/' + partfile + '.txt') 

sleep(5)	#change ver11 from 10
	
workfile = '/home/pi/icons/' + month + day + '.txt'
f = open(workfile, 'r')
	
files = []

for i in f: 
    if (partfile in i):
        i = i.strip('\n')
        files.append(i)

print(files)
count = 0
for file in files:
	count+=1
	print(file)

filename = partfile + '_'
j = 1
while j <= count:
	os.system('curl -o ' + '/home/pi/icons/'+ filename + str(j) + '.jpg ' + 'https://raw.githubusercontent.com/aat145914/Test/master/' + month + '/' + filename + str(j) + '.jpg') 
	if j == count:
		break
	j+=1	

file = '/home/pi/Display_v' + str(current_ver_num) + '.py'
os.system('sudo python ' + str(file))    #/home/pi/example5.py')

