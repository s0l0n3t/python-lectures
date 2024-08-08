#-*- coding:cp1254-*-
import urllib
import os
import sys
sys.path

global try=1

def lxx(self):
  
  a1=raw_input("what url :")
  self.urllib.urlretrieve(a1,"module"+str(try))
  b=open("module").read()
  if (os.name == "posix"):
      self.os.system("mv /*/*/Desktop/module /*/*/Desktop/files ")
      try +=1
  else:
     print "coming soon"





