#-*-coding: cp1254-*-
#Coded s0l0n3t

import os
import random
import sys
sys.path


print """
        İf you wanna 126-bit password
                "Enter Anythings ! "."""
print


def oku(say):
    if (os.name == "nt" or "dos"):
        os.chdir("C://Users/©™®FURKAN™©/Desktop")
        dosya = open("key.txt","w")
        dosya.write("%s" %(say))
        open("key.txt").read()
        dosya.close()
    if (os.name == "posix"):
        os.chdir("/home/root/Desktop/")
        dosya = open("key","w")
        dosya.write("%s" %(say))
        open("key.txt").read()
        dosya.close()

def tanim():
        laps = ["a","b","c","d","e","f","g","h","j","k","l","m","n","p","r","s","t","v","w","x","v","z"]
        maps = ["@","$","€","!","#","%","&"]
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
        b1=random.shuffle(rains)
        
        print "Password : %s"%(rains)
        global rains

def tekrar():
    
    a1 = raw_input(":")
    if (a1 == "*"):
        return
    else:
        tanim()
        oku(rains)
        return
while True:

    tekrar()
    
