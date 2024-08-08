#Uygulama 1
x = 0
Personal_Maas = [1000,2000,3000,4000]

for i in Personal_Maas:
    Personal_Maas[x] += int(i*0.2)
    x+=1

print(Personal_Maas)


#Uygulama 2

Sayac = 0
Personal_Maas2= [1000,2000,3000,4000]

for i in Personal_Maas2:
    if Personal_Maas2[Sayac] < 3000:
        Personal_Maas2[Sayac] += int(i*0.2)
    elif Personal_Maas2[Sayac] >= 3000:
        Personal_Maas2[Sayac] += int(i*0.1)
    else:
        continue
    Sayac+=1

print(" Son durum:")
print(Personal_Maas2)
