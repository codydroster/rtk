import threading
import time
import gi

import io
import fileinput
import time



#f = open("stations.pos", encoding="ISO-8859-1")
f = open("/home/cody/Desktop/sol0.pos", "r+")

time_gp = 0
latitude = 0
longitude = 0
height = 0

vn = 0
ve = 0
vu = 0

contents = f.readlines()

while(True):
#	f.seek(0,0)

	line = f.readline()
	if(line is not ""):
		time_gp = int(''.join(line[0:11].split()))
		latitude = float(line[18:30])
		longitude = float(line[32:45])
		height = float(line[48:56])
		vn = float(line[135:143])
		ve = float(line[146:155])
		vu = float(line[157:165])



		print("Time:", time_gp, "Lat:", latitude, "Long:", longitude, "Height:", height, "vn:", vn, "ve:", ve, "vu", vu)
#		print("Lat:", latitude)
#		print("Time:", time_gp)

	time.sleep(.5)

#	contents = f.readlines()
#	print(contents[len(contents)-1])	

#	time.sleep(1)



