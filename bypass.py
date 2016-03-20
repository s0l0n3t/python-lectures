#-*-coding:cp1254-*-
#coding s0l0n3t

import sys
import random
import time
sys.path


def code():
    num = ["1","2","3","4","5","6","7","8","9","0"]
    abc = ["a","b","c","d","e","f","g","j","k","l","m","n","p","r","s","t","v","y","z","w"]
    retry=[random.choice(abc),random.choice(abc),random.choice(abc),random.choice(abc),random.choice(num),random.choice(num)]
    frame = [random.choice(retry)+random.choice(retry)+random.choice(retry)+random.choice(retry)+random.choice(retry)]
    a1 = int(time.clock())
    
    global retry,frame,a1
def bypassing():
    
    ret = retry
    ii =frame
    i =[random.choice(ret)+random.choice(ret)+random.choice(ret)+random.choice(ret)+random.choice(ret)]            
    for bypass in i:
        for frame1 in ii:
            if bypass not in frame1:
                print "retrying"
                return bypass

            else:
                print "Was break this firewall"
                print
                print "key: %s"%(frame1)
                print
                print "type: NAT"
                print
                a2 = int(time.clock())
                timi =a2 - a1
                if int(timi) > 60:
                    dakika = timi - 60
                    if dakika > 60:
                        saat = dakika /60
                        print "in %s hours."%(saat)
                        sys.exit()
                    else:
                        print "in %s minutes"%(dakika)
                        sys.exit()
                else:
                        print "in %s second."%(timi)
                        sys.exit()
code()  
while True:
    bypassing()
    
    
