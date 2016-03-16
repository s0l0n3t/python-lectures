#-*-coding:cp1254-*-
import random
import sys
import time
sys.path


print """ lütfen şifrenin çözümlenebilmesi için bekleyiniz. """
a =time.asctime()
print a


def tanim(right):
    ays = right
    SYNP = ["a","b","c","d","e","f","g","j","k","l","m","n","p","r","s","t","u","v","y","z"]

    sy1 = random.choice(SYNP)
    sy2 = random.choice(SYNP)
    sy3 = random.choice(SYNP)
    sy4 = random.choice(SYNP)
    sy5 = random.choice(SYNP)
    sy6 = random.choice(SYNP)
    sy7 = random.choice(SYNP)
    sy8 = random.choice(SYNP)
    sy9 = random.choice(SYNP)
    
    
    if len(ays) == 1:
        spp1 = sy1
        print "çözümleniyor..."
        if spp1 in ays:
            print
            print a
            print ays
            sys.exit()

    if len(ays) == 2:
        spp2 = sy1 + sy2
        print "çözümleniyor..."
        if spp2 in ays:
            print
            print a
            print ays
            sys.exit()

    if len(ays) == 3:
        spp3 = sy1 + sy2 + sy3
        print "çözümleniyor..."
        if spp3 in ays:
            print
            print a
            print ays
            sys.exit()

    if len(ays) == 4:
        spp4 = sy1 + sy2 + sy3 + sy4
        print "çözümleniyor..."
        if spp4 in ays:
               print
               print a
               print ays
               sys.exit()
    if len(ays) == 5:
        spp5 = sy1 + sy2 + sy3 + sy4 + sy5
        print "çözümleniyor..."
        if spp5 in ays:
            print
            print a
            print ays
            sys.exit()

    if len(ays) == 6:
        spp6 = sy1 + sy2 + sy3 + sy4 + sy5 + sy6
        print "çözümleniyor..."
        if spp6 in ays:
            print
            print a
            print ays
            sys.exit()

    if len(ays) == 7:
        spp7 = sy1 + sy2 + sy3 + sy4 + sy5 + sy6 + sy7
        print "çözümleniyor..."
        if spp7 in ays:
            print
            print a
            print ays
            sys.exit()
    if len(ays) == 8:
        spp8 = sy1 + sy2 + sy3 + sy4 + sy5 + sy6 + sy7 + sy8
        print "çözümleniyor..."
        if spp8 in ays:
            print
            print a
            print ays
            sys.exit()

    if len(ays) == 9:
        spp9 = sy1 + sy2 + sy3 + sy4 + sy5 + sy6 + sy7 + sy8 + sy9
        print "çözümleniyor..."
        if spp9 in ays:
            print
            print a
            print ays
            sys.exit()
    
            
        

a1 = raw_input(":")
global a1
while True:
    
    tanim(a1)
    
