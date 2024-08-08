#Fonksiyonlar:
First_square_layer=255
Second_square_layer=251
Corner_fix=0


def math_func_(aim,aim2,CORNER_FIX):
    
    print(aim**2-aim2**2+CORNER_FIX)


math_func_(First_square_layer,Second_square_layer,Corner_fix)
    
    
def kare_al(Veri):
    print("Verilen ifadenin karesi: "+ str(Veri**2))

#Aynı zamanda dönüşüm yapmış oldum.
kare_al(4)

def topla(Veri1,Veri2):
    print(Veri1+Veri2)

topla(25,15)
#2 değerli fonksiyon şeması

def On_Tanimli(Veri01,Veri02=5):
    print(Veri01*Veri02)

On_Tanimli(5)
#Bu şekilde değer vermesek bile sabit bir değeri atayabiliyoruz.

def return_Using(Veri1,Veri2):
    return (Veri1*Veri2)

print(return_Using(5,4))

#Fonksiyondaki çıktıyı girdi olarak almak.

x = 15
y = 20

def Global_local_arguments(x,y):
    return x + y
#bu şekilde local değişken olduğundan üstteki tanımlamalar işe yaramamaktadır.

print(Global_local_arguments(2,3))

x = []

def Appen_List(worker1):
    x.append(worker1)

Appen_List(1)
print(x)

def sinir_kosul():
    sinir = 5000
    print(sinir == 5000)

sinir_kosul()
