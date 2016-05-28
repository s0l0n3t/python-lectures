#-*-coding:cp1254-*-
#!/usr/bin python2

import os
import time

print """ //\    /}        |  /\   
         //  \  / |s0l0n3t | /  \
        //    \/  |        |/    \
        /
"""

class user():
 name = None
 year = None
 num = ["1","2","3","4","5","6","7","8","9"]
 spec = None
	
user = user()	
	
def ask():
 isim = raw_input("Name >>")
 user.name = isim
 yas = raw_input("Year >>")
 user.year = yas
 special = raw_input("Special >>")
 user.spec = special
	
def information():
  hight1 = user.name[0].upper() + user.name[1:]
  low = [user.name, user.year, user.spec]
  low.append(hight1)
  global low
  
def write():
 password =[]
 pas1 =low[0] + low[1]
 pas2 = low[0] + low[2]
 pas3 = low[0] + low[3]
 pas4 =low[1] + low[0]
 pas5 =low[1] + low[1]
 pas6 =low[1] + low[2]
 pas7 =low[1] + low[3]
 pas8 =low[2] + low[0]
 pas9 =low[2] + low[1]
 pas10 =low[2] + low[2]
 pas11 =low[2] + low[3]
 pas12 =low[3] + low[0]
 pas13 =low[3] + low[1]
 pas14 =low[3] + low[2]
 pas15 =low[3] + low[3]
 password.append(pas1)
 password.append(pas2)
 password.append(pas3)
 password.append(pas4)
 password.append(pas5)
 password.append(pas6)
 password.append(pas7)
 password.append(pas8)
 password.append(pas9)
 password.append(pas10)
 password.append(pas11)
 password.append(pas12)
 password.append(pas13)
 password.append(pas14)
 password.append(pas15)
 dosya.write("WORDS_")
 dosya.write("\n{}".format(pas1))
 dosya.write("\n{}".format(pas2))
 dosya.write("\n{}".format(pas3))
 dosya.write("\n{}".format(pas4))
 dosya.write("\n{}".format(pas5))
 dosya.write("\n{}".format(pas6))
 dosya.write("\n{}".format(pas7))
 dosya.write("\n{}".format(pas8))
 dosya.write("\n{}".format(pas9))
 dosya.write("\n{}".format(pas10))
 dosya.write("\n{}".format(pas11))
 dosya.write("\n{}".format(pas12))
 dosya.write("\n{}".format(pas13))
 dosya.write("\n{}".format(pas14))
 dosya.write("\n{}".format(pas15))


def crate():
  if "words.txt" not in os.listdir(os.path.abspath("")):
        dosya = open("words.txt","w")
        global dosya
  else:
      print "[!] words.txt in path"
      print
      dosya = open("words.txt","w")
      global dosya

while True :
 ask()
 information()
 crate()
 write()

