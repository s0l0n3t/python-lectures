import urllib.request
import os
import time

numberVar = 0
GET_URL = "http://source.unsplash.com/random/1920x1080"


def server_connect(connect_http_addr):
	global numberVar
	numberVar+=1
	pathVar = personal_path+ os.sep + str(numberVar)+".jpg"
	connector = urllib.request.urlopen(connect_http_addr)
	driverVar = open(pathVar,"wb")
	#wb -->Binary şeklinde okuma 
	driverVar.write(connector.read())
	connector.close()
	time.sleep(2)
	driverVar.close()

personal_ = input("Number> ")
personal_path = input("Folder> ")
while True:
	if numberVar != int(personal_):
		server_connect(GET_URL)
	else:
		break
