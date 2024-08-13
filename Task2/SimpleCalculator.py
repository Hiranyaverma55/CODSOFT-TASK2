def calculator():
    print("Welcome to the simple calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponents (^)")

    
    n1 = float(input("Enter the first number n1 : "))
    n2 = float(input("Enter the second number n2: "))
    operation = input("Enter the operation (+, -, *, /,^): ")

  
    if operation == '+':
        result = n1 + n2
    elif operation == '-':
        result = n1 - n2
    elif operation == '*':
        result = n1 * n2
    elif operation == '/':
        if n2 == 0:
            print("Error: Divison can't be performed.")
            return
        result = n1 / n2
    elif operation == '^':
        result = n1 ** n2
    else:
        print("Invalid. Please choose from +, -, *, /,^.")
        return

    
    print(f"The result of {n1} {operation} {n2} is: {result}")


calculator()
