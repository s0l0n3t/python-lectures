#if

gelir_sinir = 50000
gelir = 50000

if (gelir < gelir_sinir):
    print("Gelir, beklentinin altındadır.")

#else
elif (gelir == gelir_sinir):
    print("Gelir, beklenti ile eşit durumdadır.")


else:
    print("Gelir, beklentinin altında değil.")

