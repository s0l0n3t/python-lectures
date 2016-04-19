#-*-coding: cp1254-*-
#github.com/s0l0n3t/modules

import os
import random
import sys
sys.path


print """
        Enter Anything."""
print


def read(key):
    if (os.name == "nt"):
        dosya = open("key.txt","a")
        dosya.write("\n%s" %(key))
        dosya.close()
    if (os.name == "posix"):
        dosya = open("key","a")
        dosya.write("\n%s" %(key))
        dosya.close()

def main():
        laps = ["a","b","c","d","e","f","g","h","j","k","l","m","n","p","r","s","t","v","w","x","v","z"]
        maps = ["@","$","?","!","#","%","&"]
        second = ["1","2","3","4","5","6","7","8","9","0"]
        a1=random.choice(laps)
        a2=random.choice(laps)
        a3=random.choice(laps)
        a5=random.choice(maps)
        a6=random.choice(second)
        a7=random.choice(second)
        a8=random.choice(second)
        a9=random.choice(second)
        a4=random.choice(laps)
        rains = [a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9]
       	for i in rains:
        	print "Hash : %s"%(i)
		global i

def again():
    
    a1 = raw_input(":")
    if (a1 == "*"):
        return
    else:
        main()
        read(i)
        return
while True:

    again()
    
