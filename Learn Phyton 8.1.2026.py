unit = str(input("What is your unit (cm m km)"))
number =float(input("What is your number"))
choose = str(input("Which one do you want to transform cm m km"))

if unit == "cm":
    if choose == "cm":
        print("Dont choose same units")
    elif choose == "km":
        print(number/100000)
    elif choose == "m" :
        print(number/100)
elif unit == "km":
    if choose == "km":
        print("Dont choose same units")
    elif choose == "m":
        print(number*1000)
    elif choose == "cm":
        print(number*100000)
elif unit == "m":
    if choose == "m":
        print("Dont choose same units")
    elif choose == "cm":
        print(number*100)
    elif choose == "km":
        print(number/1000)

