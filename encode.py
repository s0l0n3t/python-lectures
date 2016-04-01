#-*-coding:cp1254-*-
import os
import sys
sys.path

print """Dosya okutmayacaksan boş bırak. """

def encode():
    sy = raw_input("okunacak dosya :")
    if sy is "":
        msg =raw_input("şifre :")
        sifreli_msg="""%s"""%(msg)
    else:
        
        sifreli_msg="""%s"""%(sy)
    

    sozluk = {"a":"z", "b":"v" , "c":"w" ,
              "d":"l", "e":"n" , "f":"i" ,
              "g":"h", "ç":"s" , "ğ":"a" ,
              "h":"g", "i":"f" , "ı":"ç" ,
              "j":"d", "k":"j" , "l":"k" ,
              "m":"t", "n":"b" , "o":"e" ,
              "ö":"m", "p":"j" , "r":"p" ,
              "s":"ö", "ş":"s" , "t":"c" ,
              "u":"ş", "ü":"ı" , "v":"k" ,
              "y":"o", "z":"r"}

    sifresiz_metin = ""

    for harf in sifreli_msg:
        sifresiz_metin += sozluk.get(harf,harf)

    print sifresiz_metin
    global sifresiz_metin

def yaz():
    sor = raw_input("dosya adı :")
    dosya = open(sor,"a")
    dosya.write(":%s"%(sifresiz_metin))
    dosya.close


encode()
yaz()
    
    

