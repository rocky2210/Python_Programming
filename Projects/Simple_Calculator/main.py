from calculator import Calculator
calculator = Calculator()  # Create an instance of the Calculator class

while True:

    # header = calculator.header() #Header 

    calculator.menu()  # Display the menu

    choice = calculator.menuchoice()

    # Exit
    if choice == 6:
        print("bye..")
        print("bye...!")
        print("bye......!")
        break

    # Invalid choice
    # if choice > 6 or choice < 1:
    #     print(f"\nInvalid choice {choice}")
    #     continue

    # Choice
    if choice != 5:
        try:
            num1 = int(input("Enter the number 1: "))
            num2 = int(input("Enter the number 2: "))
        except ValueError:
            print("Value error! please enter valid numbers")
            continue
    else:  # Previous result
        print(f"previous result: {calculator.result}")
        num1 = calculator.result
        try:
            num2 = int(input("Enter the number 2: "))
            choice=calculator.menuchoice()
        except ValueError:
            print("Value error! please enter valid numbers")
            continue
        
    # Choice cases
    if choice == 1:
        result = calculator.add(num1, num2)
        message = f'Addition of {num1} and {num2} is:'
        calculator.boxoutput(message, result)
    elif choice == 2:
        result = calculator.sub(num1, num2)
        message = f'Subtraction of {num1} and {num2} is:'
        calculator.boxoutput(message,result)
    elif choice == 3:
        result = calculator.mul(num1, num2)
        message = f"Multiplication of {num1} and {num2} is"
        calculator.boxoutput(message,result)
    elif choice == 4:
        if num2 == 0:
            print("Error division by zero")
        else:
            result = calculator.div(num1, num2)
            message = f"Division of {num1} and {num2} is"
            calculator.boxoutput(message,result)
