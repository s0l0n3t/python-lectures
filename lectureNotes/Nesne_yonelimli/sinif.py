#Nesne yönelimli programlama

class testClass():
    print("Bu bir sınıftır.")

class testClass2():
    testattrb = ""
    testattrb2 = True
    testattrb3 = 0
    testattrb4 = []

testClass2.testattrb2 = False
testClass2.testattrb3 = 5


mathLesson = testClass2.testattrb
mathLesson1 = testClass2()

print(mathLesson1.testattrb2)

class testClass3():
    diller = ["turkce","ingilizce","rusca"]
    bolum = ""
    durum = True
    deneyim = 0
    def __init__(self):
        self.diller = []
        self.bolum = ""
        self.deneyim = 0
        self.durum = True
#Örneklendirme yapabiliriz bu şekiilde.__init__ self örneklendirmeyi temsil eder.


langLesson = testClass3()
langLesson.diller = ["turkce","ingilizce"]

langLesson2 = testClass3()
langLesson2.diller.append("almanca")

langTest1 = testClass3()
langTest1.bolum = "bilg. muh"
langTest1.durum = False
langTest1.deneyim = 5

print(langLesson.diller)
print(langTest1.bolum)
print(langTest1.deneyim)

class Sirket():
    calisanlar = []
    def __init__(self):
        self.bolum = []
        self.kimlik = 0
    def bolumEkle(self,yeni_bolum): #Bolum ekleme fonksiyonu
        self.bolum.append(yeni_bolum)
    
testPersonal1 = Sirket()
testPersonal1.bolumEkle("C#")
testPersonal1.kimlik = 12312415123

print(testPersonal1.bolum)
print(testPersonal1.kimlik)

