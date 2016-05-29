#-*-coding:cp1254-*-
#!/usr/bin python2
#github.com/s0l0n3t/modules

import os
import time

logo =""" //\    /bin            *     /\   /tmp
         //  \  / s0l0n3t  /  \  /      /mnt
        // /usr   \/     *     /    \ /     /etc
        /  /                 """
print logo

class user():
 name = None
 year = None
 special = None
	
user = user()	
#Burada kullanım açısından daha iyi olması amacıyla sınıfa aldım.

def ask():
 dname = raw_input("INPUT[1] >> ")
 user.name = dname
 year = raw_input("INPUT[2] >> ")
 user.year = dyear
 dspecial = raw_input("INPUT[3] >> ")
 user.spec = dspecial
#Kullanıcıdan 3 giriş alıyor.

def information():
  hight1 = user.name[0].upper() + user.name[1:]
  low = [user.name, user.year, user.spec ,hight1]
  global low
  
def write():
 pas1 =low[0] + low[1]
 pas2 =low[0] + low[2]
 pas3 =low[0] + low[3]
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
#Permütasyonlar
 time.sleep(0.1)
 dosya.write("\nWORDS_")
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
#Tün permütasyonları tek tek yazıp, dosyaya yazdırıyor.

def crate():
  if "words.txt" not in os.listdir(os.path.abspath("")):
          dosya = open("words.txt","a")
          global dosya
  else:
          print "[!] words.txt in path"
          print
          num = "1"
          dosya = open("words"+ num + ".txt","a")
          global dosya
#Eğer path üzerinde words.txt dosyası var ise oluşturuyor yoksa başına 1 ekliyor.

ask()
information()
crate()
write()
#While döngüsü koymadım çünkü GUI kapanmadan yazmıyor.

