def calculator(number1,number2,operator):
    """The function calculator() takes three parmeters and calculates the equation given by the user. The function will return an invalid operation is the operator is something rather than adding, subtracting, multiplying, division, and exponets.
    """
    if operator == '+':
        return float(number1) + float(number2)
    elif operator == '-':
        return float(number1) - float(number2)
    elif operator == '*':
        return float(number1) * float(number2)
    elif operator == '**':
        return float(number1) ** float(number2)
    elif operator == '/':
        return float(number1) / float(number2)
    else:
        return "Invalid Operation"

def parse_input():
    """The parse_input() functions takes the inputs from the user and calls the Calculator() function to calculate the equation entered by the user.
    """
    number1,operator,number2=input("Enter equation: ").split()
    print(calculator(number1,number2,operator))



