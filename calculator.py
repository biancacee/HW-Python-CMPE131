def calculator(number1, number2, operator):
    """This function takes in three arguements from the user. The function will determine if the user entered the operation to +,-,/,//,**. The function also determines if the user entered an invalid operation. 
    """
    if operator == "+": # if statements determines operation entered
        return float(number1) + float(number2)
    elif operator == "-":
        return float(number1) - float(number2)
    elif operator == "*":
        return float(number1) * float(number2)
    elif operator == "/":
        try: # a try and except in case the user divides by 0
            return float(number1) / float(number2)
        except ZeroDivisionError:
            return False
    elif operator == "//": #take account simple and complex division
        try: # another try and except to catch division by 0 
            return float(number1) // float(number2)
        except ZeroDivisionError:
            return False
    elif operator == "**":
        return float(number1) ** float(number2)
    else:
        return "Invalid Operation" # Invalid Operation if something rather than given operation is entered. 

def parse_input():
    """This function takes an input from the user that will then be used to call the calculator() function.
    """
    number1,operator,number2 = input("Enter equation: ").split() #split is used to read the users input
    print(calculator(number1,number2,operator)) #this line calls calculato function
