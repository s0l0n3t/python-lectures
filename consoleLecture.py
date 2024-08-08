#-*-coding:cp1254-*-
import os
import sys
sys.path

class caseful:
        def __init__(self):
             try:
              a1=raw_input("username :")
              a2=raw_input("password :")
              self.user =a1
              self.pass =a2
              table= [self.user,self.pass]
              for i in table:
                    print i 
              file=open("dt","w")
              self.file.write("id : %s"%(a1))
              self.file.write("\npw : %s"%(a2))
              self.file.close()
             except:
              if not a1 or a2:
                   return
              else:
                 self.os.system("cat /home/root/Desktop/dt")
