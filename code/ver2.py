#Rev14 Renamed repository Digital-Icon
#SHOULD NOT BE MODIFIED
#ANY CUSTOMIZATION DONE DOWNSTREAM
#WHEN PROD READY RENAME VER2.py

icons_folder = '/home/pi/icons/'
pi_folder = '/home/pi/'

import os
from time import sleep

#Look for icons.txt file and remove 
filelist = [ f for f in os.listdir(icons_folder) if (f.endswith('.txt'))]		
for f in filelist:
	os.remove(icons_folder+f)		

#D/l new ver.txt file and put in icons folder
cmd = 'curl -o ' + icons_folder + 'ver.txt ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/ver.txt'
os.system(cmd) 

sleep(5)	

#Open existing ver.txt file
workfile1 = pi_folder + 'ver.txt'
f = open(workfile1, 'r')	

current_ver_num = []

#Check existing version in pi folder
for i in f: 
	i = i.strip('\n')
	current_ver_num.append(i)
		
print(current_ver_num)

#Check new version in icons folder
workfile2 = icons_folder+ 'ver.txt'
f = open(workfile2, 'r')	

git_ver_num = []

#Determine git version
for i in f: 
	i = i.strip('\n')
	git_ver_num.append(i)
		
print(git_ver_num)

if current_ver_num == git_ver_num: 

	print("No version change")
	#Call readingfromfilelnx_v(current_ver_num)
	cmd = 'sudo python' + ' ' + icons_folder + 'readingfromfilelnx_v' + str(current_ver_num) + '.py' #need to include 
	os.system(cmd)
	
else:
	
	#Display update image #new ver 13
	iconimg = '/home/pi/newver.jpg'
	os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose ' + iconimg)
	
	#update ver.py, but d/l ver2.py, will be renamed later
	file5 = icons_folder + 'ver2.py'
	gitfile5 = 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/ver2.py'
	cmd5 = 'curl -o ' + file5 + ' ' + gitfile5
	os.system(cmd5)
	sleep(5)
	
	#make array --> integer
	s = ''.join(map(str,git_ver_num))
	git_ver_num = int(s)
	print(git_ver_num)
	s = ''.join(map(str,current_ver_num))
	current_ver_num = int(s)
	print(current_ver_num)
		
	#remove existing ver.txt file in pi folder
	filelist = [ f for f in os.listdir(pi_folder) if (f.endswith('ver.txt'))]
	for f in filelist:
		os.remove(pi_folder+f)					
		
	#also remove .py files in pi_folder and icons_folder	
	cmd = 'sudo rm ' + icons_folder + 'readingfromfilelnx_v' + str(current_ver_num) + '.py'
	os.system(cmd)
	
	cmd = 'sudo rm ' + pi_folder + 'Easter.py'		#ver 10
	os.system(cmd)
	
	cmd = 'sudo rm ' + pi_folder + 'Display_v' + str(current_ver_num) + '.py'
	os.system(cmd)
	
	#Remove and update starup images in startup folder, ver 13 
	startupfolder='/home/pi/startup/'
	filelist = [ f for f in os.listdir(startupfolder) if (f.endswith('.jpg'))]
	for f in filelist:
		os.remove(startupfolder+f)
			
	#update ver.txt file by moving to pi folder
	cmd2 = 'sudo cp -p ' + icons_folder + 'ver.txt ' + pi_folder
	os.system(cmd2)
	
	#download new ver num .py code
	file1 = icons_folder + 'readingfromfilelnx_v' + str(git_ver_num) + '.py'
	gitfile1 =  'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/readingfromfilelnx_v' + str(git_ver_num) + '.py'
	cmd3 = 'curl -o ' + file1 + ' ' + gitfile1
	os.system(cmd3) 
	sleep(5)
	
	file2 = pi_folder + 'Easter.py'		#ver 10
	gitfile2 = 'Easter.py'				
	cmd4= 'curl -o ' + file2 + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/' + gitfile2
	os.system(cmd4)
	sleep(5)
	
	file3 = pi_folder + 'Display_v' + str(git_ver_num) + '.py'
	gitfile3 = 'Display_v' + str(git_ver_num) + '.py'
	cmd5 = 'curl -o ' + file3 + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/' + gitfile3 #this is example5 right now
	os.system(cmd5) 
	sleep(5)
	
	#Check tft resolution, ver 13
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
	f.close()
	
	#look at startup.txt file for startup icons list
	from random import randint
	file4 = startupfolder
	os.system('curl -o ' + file4 + 'startup.txt ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/startup/'+current_tft_res+'/startup.txt') 
	sleep(5)			#ver 11
	workfile = '/home/pi/startup/startup.txt'
	f = open(workfile, 'r')
	count = 0
	for i in f:
		count+=1
	f.close()	
	j=1
	#d/l all startup images from /code/startup/
	while j<=count:
		os.system('curl -o ' + '/home/pi/startup/startup_' + str(j) + '.jpg ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/code/startup/'+current_tft_res+'/startup_'+ str(j) + '.jpg') 
		sleep(3)
		if j == count:
			break
		j+=1
	#choose randomized startup icon to display to continue
	file = randint(1,count)
	iconimg = '/home/pi/startup/' + 'startup_' + str(file) + ".jpg"
	os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose ' + iconimg)
	
	#finished updating files from new ver, proceed to call readingfromfilelnx_v(git_ver_num)
	print("Downloaded and moved new files")
	cmd = 'sudo python' + ' ' + icons_folder + 'readingfromfilelnx_v' + str(git_ver_num) + '.py'
	os.system(cmd)
