#-*- coding:cp1254-*-
import urllib
import os
import sys
sys.path

try=1
global try

def lxx(self):
  
  a1=raw_input("what url :")
  self.urllib.urlretrieve(a1,"module"+str(try))
  b=open("module").read()
  if (os.name == "posix"):
      self.os.system("mv /home/root/Desktop/module /home/root/Desktop/files ")
      try +=1
  else:
     print "coming soon"





