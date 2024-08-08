# Break & Continue
Personal_income = [8000,5000,2000,1000,3000,7000,1000]
Personal_income.sort()

for i in Personal_income:
    if i == 3000:
        print("Stopped.")
        continue
    else:
        print(i)

for i in Personal_income:
    if i == 3000:
        print("Stopped.")
        break
    else:
        print(i)

