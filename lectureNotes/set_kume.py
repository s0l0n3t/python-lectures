#Veri tipi- setler_kümeler

#sırasız.
#değiştirilebilir.
#eşsizdir.
#Farklı veri tipleri içerebilir.

set_tolist = ["0x0A","0x0A"]
set1 = set(set_tolist)

string_toset = "There are too much."

set_Typestring = set(string_toset)
print(set1)
print(set_Typestring)
Add_float = 000.1
set_Typestring.add(Add_float)
print(set_Typestring)

set_Typestring.remove(Add_float)

#difference --> 2 küme farkı

set_diff_1=set([20,11,22,44])
set_diff_2=set([15,77,88,99])

print(set_diff_1.difference(set_diff_2))


print(set_diff_2.difference(set_diff_1))

print(set_diff_1.symmetric_difference(set_diff_2))

#intersection --> kesişim.

print(set_diff_1.intersection(set_diff_2))

print(set_diff_1 & set_diff_2)

#union --> birleşim

print(set_diff_1.union(set_diff_2))

#sorgular

print(set_diff_1.isdisjoint(set_diff_2)) #kesişim boş küme mi

print(set_diff_1.issubset(set_diff_2)) #alt kümesi mi
print(set_diff_1.issuperset(set_diff_2)) #kapsıyor mu?

lis=["a",10,"b"]
lis[0]=1
print(lis)