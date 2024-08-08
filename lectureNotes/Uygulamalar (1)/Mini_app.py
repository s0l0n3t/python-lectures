#Mini application
#       STORE APPLICATION

AWARD = False
INCOME_LIMIT=  150000
magaza_= input("mağaza adı: ")
Personal_income = input("income: ")

if (int(Personal_income) > INCOME_LIMIT):
    AWARD = True

elif (int(Personal_income) < INCOME_LIMIT):
    AWARD = False

else:
    AWARD = False



if (AWARD == True):
    print("You can take an award.")

else:
    print("Another time to get award.")