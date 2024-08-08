#hatalar / istisnalar(exceptions)

a = 5
b = 0

try:
    print(a/b)

except ZeroDivisionError:
    print("Paydada sıfır olmaz.")

#tip hatası

a_ = 10
b_ = "5"
try:
    
    print(a_+b_)

except TypeError:
    print("tip hatası almaktasınız.")


#Alıştırma_1
A = [[1,2],[3,4],[5,6]]
print(list(map(lambda x: x[0]*3, A)))

