import sys
import os
from datetime import date, timedelta
import datetime


def Eastercheck():
	today = date.today()
	day = today.day
	month = today.month
	year = today.year
	
	#day = 26		#testing
	#month = 2		#testing
	#year = 2017
	
	if day<10:
		day = str(day)
		day = "0" + day
	if month<10:
		month = str(month)
		month = "0" + month
	
	day = str(day)
	month = str(month)	
	year = str(year)
	files = []

	#year = str(2017)  		#testing
	
	#Figure out what date corresponds to Easter for a given year
	workfile = '/home/pi/Easterdate.txt'
	f = open(workfile, 'r')

	for i in f:
		if (year in i):
			i = i.split(":",1)[1]
			i = str(i) 
			i = i.strip('\n')
			files.append(i)

	f.close()			

	for file in files:
		file = str(file)

	firstpart, secondpart = file[:2], file[2:]
	
	#Corresponds to beginning of lent
	d = date(int(year), int(firstpart), int(secondpart)) - timedelta(days=48)		#48 for lent

	lentmnt = d.month
	lentday = d.day
	
	#Figure out how far current date from Easter date
	yday = (date(int(year), int(month), int(day)) - d).days
	print(yday)
	
	if (yday < 0):
		print("Pre Lenten season")
		
		if (date(int(year), int(month), int(day)) - d).days == -29:
			print("Prelent 1st Sunday Zacchaeus Sunday")
			return "Prelent 1st Sunday Zacchaeus Sunday"
		if (date(int(year), int(month), int(day)) - d).days == -22:
			print("Prelent 2nd Sunday Publican and Pharisee")
			return "Prelent 2nd Sunday Publican and Pharisee"
		if (date(int(year), int(month), int(day)) - d).days == -15:
			print("Prelent 3rd Sunday Prodigal Son")
			return "Prelent 3rd Sunday Prodigal Son"
		if (date(int(year), int(month), int(day)) - d).days == -8:
			print("Prelent 4th Sunday Last Judgement")	
			return "Prelent 4th Sunday Last Judgement"
		if (date(int(year), int(month), int(day)) - d).days == -1:
			print("Prelent 5th Sunday Forgiveness")
			return "Prelent 5th Sunday Forgiveness"
			
	if (yday <= 48) and (yday >= 0):
		print("In Easter season")
		#supplement icons with Easter images if any

		if (date(int(year), int(month), int(day)) - d).days == 0:
			print("Clean Monday Lent Begins") 
			return "Clean Monday Lent Begins"
		if (date(int(year), int(month), int(day)) - d).days == 5:
			print("1st Saturday St. Theodore Saturday")
			return "1st Saturday St. Theodore Saturday"
		if (date(int(year), int(month), int(day)) - d).days == 6:
			print("1st Sunday of Orthodoxy")				#1st Sunday of Great Lent
			return "1st Sunday of Orthodoxy"
		if (date(int(year), int(month), int(day)) - d).days == 13:
			print("2nd Sunday St. Gregory Palamas") 		#2nd Sunday of Great Lent
			return "2nd Sunday St. Gregory Palamas"
		if (date(int(year), int(month), int(day)) - d).days == 20:
			print("3rd Sunday Veneration of the Cross") 	#3rd Sunday of Great Lent
			return "3rd Sunday Veneration of the Cross"
		if (date(int(year), int(month), int(day)) - d).days == 27:
			print("4th Sunday St. John Climacus") 			#4th Sunday of Great Lent
			return "4th Sunday St. John Climacus"
		if (date(int(year), int(month), int(day)) - d).days == 33:
			print("5th Saturday the Theotokos Akathist") 
			return "5th Saturday the Theotokos Akathist"
		if (date(int(year), int(month), int(day)) - d).days == 34:
			print("5th Sunday St. Mary of Egypt") 			#5th Sunday of Great Lent	
			return "5th Sunday St. Mary of Egypt"
		if (date(int(year), int(month), int(day)) - d).days == 40:
			print("6th Saturday Lazarus") 
			return "6th Saturday Lazarus"
		if (date(int(year), int(month), int(day)) - d).days == 41:
			print("Palm Sunday")
			return "Palm Sunday"

		if (date(int(year), int(month), int(day)) - d).days == 42:
			print("Holy Monday")
			return "Holy Monday"			 
		if (date(int(year), int(month), int(day)) - d).days == 43:
			print("Holy Tuesday")
			return "Holy Tuesday"
		if (date(int(year), int(month), int(day)) - d).days == 44:
			print("Holy Wednesday")
			return "Holy Wednesday"		 
		if (date(int(year), int(month), int(day)) - d).days == 45:
			print("Holy Thursday Last Supper")
			return "Holy Thursday Last Supper"			
		if (date(int(year), int(month), int(day)) - d).days == 46:
			print("Holy Friday The Passion") 
			return "Holy Friday The Passion"
		if (date(int(year), int(month), int(day)) - d).days == 47:
			print("Holy Saturday")
			return "Holy Saturday"
		if (date(int(year), int(month), int(day)) - d).days == 48:
			print("Easter Sunday")
			return "Easter Sunday"
	
	if (yday <= 97) and (yday > 48):
		print("Past Easter season")
		
		if (date(int(year), int(month), int(day)) - d).days == 55:			#2nd Sunday of Easter
			print("Second Sunday of Pascha Thomas Sunday")				
			return "Second Sunday of Pascha Thomas Sunday"
		if (date(int(year), int(month), int(day)) - d).days == 62:			#3rd Sunday of Easter
			print("Third Sunday of Pascha Sunday of the Myrrhbearers")
			return "Third Sunday of Pascha Sunday of the Myrrhbearers"
		if (date(int(year), int(month), int(day)) - d).days == 69:			#4th Sunday of Easter
			print("Fourth Sunday of Pascha Sunday of the Paralytic")
			return "Fourth Sunday of Pascha Sunday of the Paralytic"
		if (date(int(year), int(month), int(day)) - d).days == 72:			
			print("Mid Pentecost 25 days after Pascha")
			return "Mid Pentecost 25 days after Pascha"
		if (date(int(year), int(month), int(day)) - d).days == 76:			#5th Sunday of Easter
			print("Fifth Sunday of Pascha Sunday of the Samaritan Woman")
			return "Fifth Sunday of Pascha Sunday of the Samaritan Woman"
		if (date(int(year), int(month), int(day)) - d).days == 83:			#6th Sunday of Easter
			print("Sixth Sunday of Pascha Sunday of the Blind Man")
			return "Sixth Sunday of Pascha Sunday of the Blind Man"
		if (date(int(year), int(month), int(day)) - d).days == 88:			
			print("Feast of the Ascension 40 days after Pascha")
			return "Feast of the Ascension 40 days after Pascha"
		if (date(int(year), int(month), int(day)) - d).days == 90:			#7th Sunday of Easter	
			print("Seventh Sunday of Pascha Sunday of the Holy Fathers")
			return "Seventh Sunday of Pascha Sunday of the Holy Fathers"
		if (date(int(year), int(month), int(day)) - d).days == 97:
			print("Pentecost 50 days since Pascha")
			return "Pentecost 50 days since Pascha"

	if (yday <= 111) and (yday > 97):
		print("Past Pentecost")
		
		if (date(int(year), int(month), int(day)) - d).days == 98:
			print("Monday of the Holy Spirit")
			return "Monday of the Holy Spirit"	
		if (date(int(year), int(month), int(day)) - d).days == 104:			#1st Sunday after Pentecost
			print("First Sunday after Pentecost All Saints Sunday")
			return "First Sunday after Pentecost All Saints Sunday"
		if (date(int(year), int(month), int(day)) - d).days == 105:
			print("Apostles' Fast Second Monday after Pentecost")
			return "Apostles' Fast Second Monday after Pentecost"
		if (date(int(year), int(month), int(day)) - d).days == 111:			#2nd Sunday after Pentecost
			print("Second Sunday after Pentecost All Saints of North America Sunday")
			return "Second Sunday after Pentecost All Saints of North America Sunday"
	
	else:
		print("Not in Easter season")
		return False
		