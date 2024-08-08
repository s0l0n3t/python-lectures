#Fonksiyonel Programlama

TestA = 6

def impure_sum(exP1):
    return exP1*TestA

def pure_sum(Exp1):
    return Exp1 + TestA

print(impure_sum(5))

#Map & filter & reduce

liste = [1,2,3,4,5,6,7]

for i in liste:
    print(i + 10)


list(map(lambda x: x + 10, liste))

#filter

liste2 = [0,1,2,3,4,5,6,7,8,9]

print(list(filter(lambda x: x % 2 == 0, liste2)))

for i in liste2:
    if (i%2 == 0):
        print(i)
#Bunlar aynı işlevi görüyor.(filter ile)

#REDUCE

from functools import reduce

liste3 = [0,1,2,3,4,5]

print(reduce(lambda a,b: a + b,liste3))
#hepsini sıra sıra topladı.

