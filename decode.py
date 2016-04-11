#-*-coding:cp1254-*-
import sys
sys.path

print """Dosya okutmayacaksan bos birak. """

def decode():
    sy = raw_input("okunacak dosya :")
    if sy is "":
        msg =raw_input("sifre :")
        sifreli_msg="""%s"""%(msg)
    else:
        
        sifreli_msg="""%s"""%(sy)
    

    
    

    sozluk = {"z":"a", "v":"b" , "w":"0" ,
              "l":"d", "n":"e" , "i":"f" ,
              "h":"g", "c":"s" , "i":"a" ,
              "g":"h", "c":"w" ,"f":"j",
              "j":"k" , "k":"l" ,
              "t":"m", "b":"n" , "e":"o" ,
              "m":"t", "0":"p" , "p":"r" ,
              "u":"s",
              "d":"u", "y":"v" ,
              "o":"y", "r":"z"}

    sifresiz_msg = ""
    
    for harf in sifreli_msg:
         sifresiz_msg += sozluk.get(harf,harf)

    print sifresiz_msg
    global sifresiz_msg
    
def yaz():
    asg = raw_input("yazilacak dosya adi :")
    sg = open(asg+".txt","a")
    sg.write(":%s"%(sifresiz_msg))

decode()
yaz()
