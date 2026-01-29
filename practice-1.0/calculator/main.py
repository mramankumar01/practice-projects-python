# Simple Calculator

while(input("Enter 'y' to continue or 'n' to exit: ")=='y'):
    try :
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print('''Select operation:
            1. Add represented by +
            2. Subtract represented by -
            3. Multiply represented by *
            4. Divide represented by / ''')
        o = input("Enter Operator: ")

        match o:
            case '+':
                print(f"The result of {a} + {b} is: ", a + b)        
            case '-':
                print(f"The result of {a} - {b} is: ", a - b)        
            case '*':
                print(f"The result of {a} * {b} is: ", a * b)        
            case '/':
                print(f"The result of {a} / {b} is: ", a / b)        
            case default:
                print("Invalid Operator")
        
    except Exception as e:
        print("Enter a valid value for a and b")