#VERI YAPILARI

ilk_liste = ["ben","bir","sey"]

ikinci_liste=["s",2,ilk_liste]

print(ikinci_liste)

print(type(ikinci_liste[2]))

#del ikinci_liste

print(ikinci_liste[0:2])

ikinci_liste[0:2] = "bir","bir","bir"

print(ikinci_liste)

ilk_liste.append("saklı")

ikinci_liste.remove(ilk_liste)

ikinci_liste.insert(len(ikinci_liste),ilk_liste)

ilk_liste.pop(1)

print(ilk_liste.count("bir"))
print(ikinci_liste)

yedek_liste= ilk_liste.copy()   #yedeğini almış olduk.

yedek_liste.extend(["ilk","ilk"])

yedek_liste.reverse()

yedek_liste.sort()
yedek_liste.clear()

print(yedek_liste)