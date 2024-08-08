#-*-coding:cp1254-*-
import os
import sys
import random
def virus():
    
    sayi = ["a","b","c","d","e","f","g","h","j","k","l","m","n","o","i","v"]
    reg = ["1","2","3","4","5","6","7","8","9","0"]
    a= random.choice(sayi)
    b = random.choice(reg)
    dosya = open("temiz","w")
    dosya.write ("hi")
    dosya.close()
    if os.path.exists("temiz"):
        c ="temiz" + a + b
        dosya2= open(c,"w")
        dosya2.write("hi")
        dosya2.close()
        return dosya2
        
        
        
    
while True:
    virus()
    continue
