#Renamed repository Digital-Icon
#v5, this should be rename v5 in next release..
#added laststart.txt in pi folder to keep track of last time turned on..
#this is so that don't need to dl images for multiple power on's in a day..
#added code block #Last Start check# and subseqent if and else statement..
#if (only condition) and else (full block)
#v5_1: Input to Eastercheck(day, month,year)

import os
from datetime import date
from time import sleep
	

#Figure out current date
today = date.today()
day = today.day			
month = today.month
#print("Current Month/Day:")
#print(month, day)

#-------------------------------------------------TESTING-------------------------------------------------------------#
#day = 4
#month = 6
#-------------------------------------------------TESTING-------------------------------------------------------------#

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
#print("Let's see tft res")
#print(current_tft_res)

#Determine version
workfile1 = pi_folder + 'ver.txt'
f = open(workfile1, 'r')	

current_ver_num = []

for i in f: 
	i = i.strip('\n')
	current_ver_num.append(i)

s = ''.join(map(str,current_ver_num))
current_ver_num = int(s)
#print("Let's see version number")
#print(current_ver_num)
#end versioning

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

	#New instead of adding in ver2.py		#moved in one tab
	pi_folder = '/home/pi/'		
	file4 = pi_folder + 'Saints.py'		
	gitfile4 = 'Saints.py'
	cmd6 = 'curl -o ' + file4 + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/' + gitfile4
	os.system(cmd6) 
	sleep(5)	

	#GET NEW CUSTOMIZATION FILE, Git V5
	icons_folder = '/home/pi/icons/'
	file4 = icons_folder + 'subproc_test_v' + str(current_ver_num) + '.py'
	gitfile4 = 'subproc_test_v' + str(current_ver_num) + '.py'
	cmd6 = 'curl -o ' + file4 + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/' + gitfile4 
	os.system(cmd6) 
	sleep(5)

	#New Git V5
	file5 = pi_folder + 'laststart.txt'
	gitfile5 = 'laststart.txt'
	cmd7 = 'curl -o ' + file5 + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/' + gitfile5
	os.system(cmd7) 
	sleep(5)
	
	#New Git V5
	os.remove('/home/pi/startup.sh') 
	file6 = pi_folder + 'startup.sh'
	gitfile6 = 'startup.sh'
	cmd8 = 'curl -o ' + file6 + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/' + gitfile6
	os.system(cmd8) 
	sleep(5)
	#need to add this
	cmd9 = 'chmod +x /home/pi/startup.sh'
	os.system(cmd9)
	sleep(1)
	

import sys
sys.path.append('/home/pi')
#Check if in Easter season
from Easter import Eastercheck 
Chk = Eastercheck(0,0,0)		#new args VER5
#If are in Easter season, replace spaces with dash
if Chk:
	Chk = Chk.replace(" ", "-")

#print(Chk)
#day = 26				#testing
#month = 2

#Check if current day's icons exist
if month < 10:
	monthchk = "0" + str(month)
else:
	monthchk = str(month)
if day < 10:
	daychk = "0" + str(day)
else:
	daychk = str(day)	
print("MID HERE")
print(monthchk, daychk)
same_as_curr_day = False  #Important declaration here
workfile = '/home/pi/icons/'+str(monthchk) + str(daychk) + '.txt'
import sys
sys.path.append(workfile)
print(workfile)
import os.path
print("OS PATH")
print(os.path.exists(workfile))
if os.path.exists(workfile):
	same_as_curr_day = True
#Rewrite last saved file
else:
	curr = daychk + "-" + monthchk
	pi_folder = '/home/pi/'
#Removed V5git
#	workfile2 = pi_folder + 'laststart.txt'
#	with open(workfile2, 'w') as the_file:
#		the_file.write(curr)
#		the_file.close()
print("HERE")
print(same_as_curr_day)
	
if not same_as_curr_day:			#if (new v5)
	
	#Remove all icons from last start, removed new ver5
#	filelist = [ f for f in os.listdir('/home/pi/icons') if (f.endswith('.jpg') or f.endswith('.txt'))]
#	for f in filelist:
#		os.remove('/home/pi/icons/'+f)

	#Proceed if in Easter season	
	if Chk:
		textfilepath = '/home/pi/icons/' + Chk + '.txt'
		if not os.path.exists(textfilepath):
			print("ENTERED 1")
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
			count = 0						#now starts at 0, ver4
			#Count number of Easter feast .jpgs to d/l
			for file in files:
				count+=1
				print(file)		
		
			filename = Chk + '_'
			j = 0							#now starts at 0, ver4
			#D/l Easter feast icons
			while j < count:				#now < not <=, ver4
				os.system('curl -o ' + '/home/pi/icons/'+ filename + str(j) + '.jpg ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res +'/' +'Easter' + '/' + filename + str(j) + '.jpg') 
				if j == (count-1):			#now count-1 from count, ver4
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
	pathtopartfile = pi_folder + '/icons/' + partfile
	textfilepathfile = pathtopartfile + '.txt'
	
	if not os.path.exists(textfilepathfile):
		print("ENTERED 2")
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

		for file in files:
			os.system('curl -o ' + '/home/pi/icons/'+ file + ' ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res +'/' + month + '/' + file) 

	#Call Display_v(current_ver_num)	
	file = '/home/pi/Display_v' + str(current_ver_num) + '.py'
	os.system('sudo python ' + str(file))    
else: 			
	#new v5
	#Call Display_v(current_ver_num)		
	file = '/home/pi/Display_v' + str(current_ver_num) + '.py'
	os.system('sudo python ' + str(file))    

