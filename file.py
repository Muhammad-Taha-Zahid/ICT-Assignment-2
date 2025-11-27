def Smart_Calculator():
    print("Smart Calculator")
    
    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")
    operation = input("Enter the operation (+, -, *, /): ")
    
    try:
        n1 = float(num1_input)
        n2 = float(num2_input)
    except ValueError:
        print("Error: Please enter valid numeric values for both numbers.")
        return
    
    result = None
    
    if operation == '+':
        result = n1 + n2
    
    elif operation == '-':
        result = n1 - n2
    
    elif operation == '*':
        result = n1 * n2
    
    elif operation == '/':
        if n2 == 0:
            print("Error: Cannot divide by zero.")
            return
        else:
            result = n1 / n2
    
    else:
        print(f"Error: Invalid operation '{operation}'.")
        return
        
    print("--- Result ---")
    print(f"The calculation is: {n1} {operation} {n2}")
    print(f"The result is: {result}")

Smart_Calculator()