#take inputs from user
input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second "))
operator = input("Enter an operator: ")

if operator not in ['+', '-', '*', '/', '%']:
    print("Invalid operator. Please use between +, -,*, /,%")
else:
    if operator == '+':
        print("Result is ", input1 + input2)
    elif operator == '-':
        print("Result is ", input1 - input2)
    elif operator == '*':
        print("Result is ", input1 * input2)
    elif operator == '/':
        if input2 == 0:
            print("Division by zero is not allowed")
        else:
            print("Result is ", input1 / input2)
    elif operator == '%':
        print("Result is ", input1 % input2)
    else:
        print("Invalid Inputs")