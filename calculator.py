# Simple Calculator (Run Again and Again)

while True:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation")
    print("1 Addition (+)")
    print("2 Subtraction (-)")
    print("3 Multiplication (*)")
    print("4 Division (/)")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        print("Result =", num1 + num2)

    elif choice == '2':
        print("Result =", num1 - num2)

    elif choice == '3':
        print("Result =", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero not allowed")

    elif choice == '5':
        print("Calculator closed")
        break

    else:
        print("Invalid choice")

    print("\n---------------------\n")
