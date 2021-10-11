def Calculator(number1, number2, operator):
    if operator == "+":
        return float(number1) + float(number2)
    elif operator == "-":
        return float(number1) - float(number2)
    elif operator == "*":
        return float(number1) * float(number2)
    elif operator == "/":
        return float(number1) / float(number2)
    elif operator == "**":
        return float(number1) ** float(number2)
    else:
        return "Invalid Operation"

def parse_input():
    number1,operator,number2 = input("Enter equation: ").split()
    print(Calculator(number1,number2,operator))


