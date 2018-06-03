#Need to fix, writing new date in readingfromfilelnx before this file is called

from datetime import date
import calendar
import os
from time import sleep

import sys
sys.path.append('/home/pi')
from Easter import Eastercheck 

#Gets today's date
today = date.today()
#-------------------------------------------------TESTING-------------------------------------------------------------#
day = today.day
month = today.month

#-------------------------------------------------TESTING-------------------------------------------------------------#
#day = 17
#month = 8
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

#current day/month
if month < 10:
	monthchk = "0" + str(month)
else:
	monthchk = str(month)
if day < 10:
	daychk = "0" + str(day)
else:
	daychk = str(day)	

path = '/home/pi/icons/'

#Deleting function called first
def del_main(day, month):
	
	monthcheck = makestring(month)
	daycheck = makestring(day)
	curr_monthday = str(monthcheck) + str(daycheck)
	
	#Testing
	#path = '/home/pi/icons/'
	
	#Check last start date
	pi_folder = '/home/pi/'
	workfile2 = pi_folder + 'laststart.txt'
	f = open(workfile2, 'r')
	last_start = []
	for i in f: 
		i = i.strip('\n')
		last_start.append(i)
	s = ''.join(map(str,last_start))
	last_start = str(i)
	#print(last_start)

	last_start_day, last_start_month = last_start.split('-')

	#TEST
	#last_start_day =28
	#last_start_month = 3
	#last_start_day = makestring(last_start_day)
	#last_start_month = makestring(last_start_month)
	
	daysdelarray = []
	#Find days in previos month
	days_of_last_month = daysofmonth(str(last_start_month))
	
	#Chk = Eastercheck(0,0,0)
	#If are in Easter season, replace spaces with dash
	#if Chk:
	#	Chk = Chk.replace(" ", "-")
	#	print(Chk)
		
	#want to delete icons/txt files the 7 days following the last start date
	#if current day within the 7 days break earlier
	#Added Git V5
	days_left=0
	#check if last start falls 7 days before end of month
	if (((int(day) - int(last_start_day))>0) and (monthcheck == last_start_month)):
		for i in range(int(last_start_day), int(day), 1): #int(last_start_day)+7
			print("ENTERED FIRST DEL LOOP")
			dayi = makestring(i)
			last_start_month=makestring(last_start_month)
			
			last_start_monthday = last_start_month + dayi
			
			#Break out of loop if same as current day
			if (last_start_monthday == curr_monthday):
				break	
			
			Chk = Eastercheck(int(dayi),int(last_start_month),0)
			if Chk:
				Chk = Chk.replace(" ", "-")
				Chk = str(Chk) + '.txt'
				daysdelarray.append(Chk)
				print(Chk)
			
			daytodelete = last_start_month + dayi + '.txt'
			daysdelarray.append(daytodelete)
	
		days_left=0
	
	if ((monthcheck != last_start_month) and ((int(monthcheck)-int(last_start_month))!=1)):
		
		#FULL DELETE
		print("IN FULL DELETE")
		icons_folder = '/home/pi/icons/'
		currmonthdayfile = curr_monthday + '.txt'
		filelist = [ f for f in os.listdir(icons_folder) if (f.endswith('.txt'))]		
		for f in filelist:
			if ((f != currmonthdayfile) and (f != 'ver.txt')):
				os.remove(icons_folder+f)
		filelist = [ f for f in os.listdir(icons_folder) if (f.endswith('.jpg'))]		
		for f in filelist:
			if  curr_monthday in f:
				continue
			else:
				os.remove(icons_folder+f)
		
	
	#if not, must be < 7 days before end of month
	if (monthcheck != last_start_month) and ((int(monthcheck)-int(last_start_month))==1):
		for i in range(int(last_start_day), int(days_of_last_month)+1, 1):
			print("ENTERED SECOND DEL LOOP")
			dayi = makestring(i)
			last_start_month=makestring(last_start_month)			

			#days_left = 7 - (days_of_last_month - int(last_start_day))
			days_left = int(day)
			print(days_left)
			last_start_monthday = last_start_month + dayi

			if (last_start_monthday == curr_monthday):
				days_left=0
				break
			
			Chk = Eastercheck(int(dayi),int(last_start_month),0)
			if Chk:
				Chk = Chk.replace(" ", "-")
				Chk = str(Chk) + '.txt'
				daysdelarray.append(Chk)
				print(Chk)
			
			daytodelete = last_start_month + dayi + '.txt'
			daysdelarray.append(daytodelete)
			
		print(days_left)
	
	#these are leftover days between those to end last month and 7 days
	if days_left:
		nextmonth = int(last_start_month) + 1
		if nextmonth == 13:
			nextmonth = 1
		for i in range(1, int(days_left), 1):
			
			dayi = makestring(i)
			nextmonth=makestring(nextmonth)	
			
			nextdaymonth = str(nextmonth) + dayi

			if (nextdaymonth == curr_monthday):
				days_left=0
				break
			
			Chk = Eastercheck(int(dayi),int(nextmonth),0)
			if Chk:
				Chk = Chk.replace(" ", "-")
				Chk = str(Chk) + '.txt'
				daysdelarray.append(Chk)
				print(Chk)				
				
			daytodelete = nextmonth + dayi + '.txt'
			daysdelarray.append(daytodelete)
	
	print("Days to delete:")
	print(daysdelarray)
	
	#Compiles all files with that date in the filename
	filelist = []
	for textfile in daysdelarray:
		workfile = path + textfile
		try:
			f = open(workfile, 'r')
		except:
			print("No such file")
		date= textfile.strip('.txt')
		for i in f:
			if (date in i):
				i = i.strip('\n')
				filelist.append(i)
	print("Delete List:")		
	print(filelist)
	
	#Deletes all files with that date in the filename
	for f in filelist:
		try:
			os.remove(path+f)
			print("File deleted:")
			print(path+f)
		except:
			print("File not found")
	
	#Delete textfile last
	for textfile in daysdelarray:
		try:
			os.remove(path+textfile)
			print("File deleted")
		except:
			print("File not found")	
	#delete all Easter files
	#inside above code
	
	#next begin downloading next 7 days
	
def dl_main(day, month,current_tft_res):
	
	monthcheck = makestring(month)
	daycheck = makestring(day)
	curr_monthday = str(monthcheck) + str(daycheck)

	#TEST
	#monthcheck = makestring(3)
	#daycheck = makestring(28)
	#curr_monthday = str(monthcheck) + str(daycheck)
	#path = '/home/pi/icons/testing/'
	
	daysdlarray = []
	daysdlarrayE=[] #Easter
	days_of_current_month = daysofmonth(str(monthcheck))
	
	import sys
	sys.path.append('/home/pi')
	from Easter import Eastercheck 
	#Chk = Eastercheck(0,0,0)
	#If are in Easter season, replace spaces with dash
	#if Chk:
	#	Chk = Chk.replace(" ", "-")
	#	print(Chk)
		
	#want to download (dl) icons/txt files the 7 days following the current date

	if (days_of_current_month - int(daycheck))>7:
		for i in range(int(daycheck)+1, int(daycheck)+8, 1):
			
			dayi = makestring(i)
			future_monthday = monthcheck + dayi
			
			Chk = Eastercheck(int(dayi),int(monthcheck),0)
			if Chk:
				Chk = Chk.replace(" ", "-")
				Chk = str(Chk) + '.txt'
				daysdlarrayE.append(Chk)
				#print(Chk)
			
			daytodownload = monthcheck + dayi + '.txt'
			daysdlarray.append(daytodownload)
	
		days_left=0
		#print(daysdlarray)
	
	#if not, must be < 7 days before end of month
	if (days_of_current_month - int(daycheck))<7:
		for i in range(int(daycheck)+1, int(days_of_current_month)+1, 1):
			
			dayi = makestring(i)
			#last_start_month=makestring(last_start_month)			

			days_left = 7-(days_of_current_month - int(daycheck))
			print(days_left)
			#last_start_monthday = last_start_month + dayi
			
			Chk = Eastercheck(int(dayi),int(monthcheck),0)
			if Chk:
				Chk = Chk.replace(" ", "-")
				Chk = str(Chk) + '.txt'
				daysdlarrayE.append(Chk)
				#print(Chk)
			
			daytodownload = monthcheck + dayi + '.txt'
			daysdlarray.append(daytodownload)
		
		print(daysdlarray)	
		print(days_left)
	
	#these are leftover days between those to end last month and 7 days
	if days_left:
		nextmonth = int(monthcheck) + 1
		if nextmonth == 13:
			nextmonth = 1
		for i in range(1, int(days_left)+1, 1):
			
			dayi = makestring(i)
			nextmonth=makestring(nextmonth)	
			
			nextdaymonth = str(nextmonth) + dayi

			if (nextdaymonth == curr_monthday):
				days_left=0
				break
			
			Chk = Eastercheck(int(dayi),int(nextmonth),0)
			if Chk:
				Chk = Chk.replace(" ", "-")
				Chk = str(Chk) + '.txt'
				daysdlarrayE.append(Chk)
				print(Chk)				
				
			daytodownload = nextmonth + dayi + '.txt'
			daysdlarray.append(daytodownload)

	print(daysdlarray)
	print("Easter season array")
	print(daysdlarrayE)

	filelist = []
	filelistE = []
	for textfile in daysdlarray:
		#workfile = '/home/pi/icons/' + textfile
		month= textfile[:2]
		if os.path.exists(path+textfile):
			continue
		try:
			os.system('curl -o ' + path + textfile + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res + '/' + month + '/' + textfile) 
			sleep(4)
		except:
			print("No such file on server")
	
	for textfile2 in daysdlarrayE:
		if os.path.exists(path+textfile2):
			continue
		try:
			os.system('curl -o ' + path + textfile2 + ' https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res + '/Easter/' + textfile2) 
			sleep(4)
		except:
			print("No such file on server")	
	
	for textfile in daysdlarray:
		workfile = path + textfile
		try:
			f = open(workfile, 'r')
		except:
			print("No such file in dir")
		for i in f:
			i = i.strip('\n')
			filelist.append(i)
	
	for textfile2 in daysdlarrayE:
		workfile = path + textfile2
		try:
			f = open(workfile, 'r')
		except:
			print("No such file in dir")
		for i in f:
			i = i.strip('\n')
			filelistE.append(i)
			
	print(filelist)
	print(filelistE)

	#Download image files
	for f in filelist:
		month= f[:2]
		if os.path.exists(path+f):
			continue
		try:
			print(file)
			os.system('curl -o ' + path + f + ' ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res +'/' + month + '/' + f) 
			print("File downloaded")
		except:
			print("File not found")
	
	for f2 in filelistE:
		if os.path.exists(path+f2):
			continue
		try:
			os.system('curl -o ' + path + f2 + ' ' + 'https://raw.githubusercontent.com/aat145914/Digital-Icon/master/' + current_tft_res +'/Easter/' + f2) 
			print("File downloaded")
		except:
			print("File not found")		
	
	return
	
def makestring(i):
	if i < 10:
		i = "0" + str(i)
	else:
		i = str(i)
	return i	

def daysofmonth(monthno):
	
	if monthno in  ("01", "03", "05", "07", "08", "10", "12"):
		day_of_month = 31

	elif monthno in ("04", "06", "09", "11"):
		day_of_month = 30
		
	elif (monthno == "02") and (calendar.isleap(today.year)):
		day_of_month = 29

	else:
		day_of_month = 28

	print(day_of_month)
	return day_of_month

def rewritelastsaved():
	
	curr = daychk + "-" + monthchk
	pi_folder = '/home/pi/'
	workfile2 = pi_folder + 'laststart.txt'
	with open(workfile2, 'w') as the_file:
		the_file.write(curr)
		the_file.close()

del_main(day, month)
dl_main(day, month,current_tft_res)
rewritelastsaved()
quit()