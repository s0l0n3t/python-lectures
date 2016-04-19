#-*-coding:cp1254-*-
import sys
sys.path

print """Dosya okutmayacaksan bos birak. """

def encode():
    sy = raw_input("okunacak dosya :")
    if sy is "":
        msg =raw_input("sifre :")
        sifreli_msg="""%s"""%(msg)
    else:
        
        sifreli_msg="""%s"""%(sy)
    

    sozluk = {"a":"z", "b":"v" , "0":"w" ,
              "d":"l", "e":"n" , "f":"i" ,
              "g":"h", "c":"s" , "i":"a" ,
              "h":"g", "w":"c" ,"j":"f",
              "k":"j" , "l":"k" ,
              "m":"t", "n":"b" , "o":"e" ,
              "t":"m", "p":"0" , "r":"p" ,
              "s":"u",
              "u":"d", "v":"y" ,
              "y":"o", "z":"r"}

    sifresiz_metin = ""

    for harf in sifreli_msg:
        sifresiz_metin += sozluk.get(harf,harf)

    print sifresiz_metin
    global sifresiz_metin

def yaz():
    sor = raw_input("yazilacak dosya adi :")
    dosya = open(sor+".txt","a")
    dosya.write(":%s"%(sifresiz_metin))
    dosya.close


encode()
yaz()
    
    

