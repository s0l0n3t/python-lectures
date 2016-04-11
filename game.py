#-*-coding:cp1254-*-
#github.com/s0l0n3t/modules
import sys
import random
sys.path

logo = """
       Amac:
         Zarin sayisini bilmektir.
         Eger bilirseniz verdiginiz miktarin 2 katini kazanirsiniz.
      
**Komutlar icin Kac tl sorusuna komutlar yazınız. 
						  """
global money,name

print logo
print
class database():
       name = "User"
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
                    print "isim icin --> isim"
                    print
                    print "Bakiyenizi ogrenmek için --> bakiyem"
		    print
		    print "Kayit islemleri icin --> kayit"
		    print
		    print "Sifirlama islemi icin --> sifirla" 
	     elif soru == "sifirla":
	       database.money = 300
             elif soru == "kayit":
		  user = raw_input("kaydet yada ac :")
		  if user == "kaydet":
		      dosya = open("%s"%(database.name),"w")
		      dosya.write("%s"%(database.money))
		      dosya.close()
		      print "başarılı."
		      return
		  if user == "ac":
		     user1 = raw_input("Kullanici adi :")
		     if not user1:
			print "Lutfen bir kullanici adi girin."
			return
		     else:
			dosyam = open(user1)
			liste = dosyam.read()
			user1 = database.name
			database.money = liste
			print "%s kullanicisi bilgisi eklenmistir.(%s)"%(user1,liste)
			return
             else:
                 return
             
while True:
       
       main()
