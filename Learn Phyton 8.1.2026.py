import math

islem = str(input("What do you want to do (Calculator / Length): "))

if islem == "Calculator":
    num1 = float(input("Enter first number: "))
    num2_input = input("Enter second number (press Enter to skip for sqrt): ")
    
    if num2_input == "":
        # If no second number, automatically do sqrt
        print(math.sqrt(num1))
    else:
        num2 = float(num2_input)
        operator = str(input("Select an operation (+, -, *, /, %, ^, //): "))
        
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1 / num2)
        elif operator == "%":
            print(num1 % num2)
        elif operator == "^":
            print(num1 ** num2)
        elif operator == "//":
            print(num1 // num2)

elif islem == "Length":
    leg1 = float(input("Enter Length: "))
    legOp1 = str(input("Current unit (km, cm, m): "))
    legOp2 = str(input("Convert to (km, cm, m): "))

    if legOp1 == "km":
        if legOp2 == "cm":
            print(leg1 * 100000)
        elif legOp2 == "m":
            print(leg1 * 1000)
        else:
            print("Invalid input")
    elif legOp1 == "cm":
        if legOp2 == "km":
            print(leg1 / 100000)
        elif legOp2 == "m":
            print(leg1 / 100)
        else:
            print("Invalid input")
    elif legOp1 == "m":
        if legOp2 == "km":
            print(leg1 / 1000)
        elif legOp2 == "cm":
            print(leg1 * 100)
        else:
            print("Invalid input")
else:
    print("Invalid input")

