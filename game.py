#-*-coding:cp1254-*-
import sys
import random
sys.path

logo = """
       Amac:
         Zarin sayisini bilmektir.
         Eger bilirseniz verdiginiz miktarin 2 katini kazanirsiniz.
**Komutlar icin Kac tl sorusuna komutlar yazınız."""
global money,name

print logo
class database():
       name = "Ali"
       money = 300

database=database()

def main():
             soru = raw_input(" :")
             if not soru:
                    rau =input("Kac tl :")
                    if not rau:
                            return
                    else:
              
                     a1 = input(" (1-6 arasi)sayi :")
                     b1 = random.randrange(1,7)
                     if (a1 == b1):
                        sy =rau*2
                        print "Kazandin. Verdigin miktarin iki kati eklendi."
                        database.money+= sy 
                        print database.money
                        return
                     else:
                         print "Kaybettin. Verdigin miktar kadar azaldi."
                         database.money -= rau
                         print database.money
                         return
             elif soru == "isim":
                     print database.name
                     nick = raw_input("Yeni isim :")
                     if not nick:
                            return
                     else:
                            database.name = nick
                            return
             elif soru == "bakiyem":
                print database.money
             elif soru == "komutlar":
                    print "isim için --> isim"
                    print
                    print "Bakiyenizi ogrenmek için --> param,miktar,para,bakiyem"
             else:
                 return
             
while True:
       
       main()
