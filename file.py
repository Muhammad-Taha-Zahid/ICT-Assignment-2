import random

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


def guessing_game():
    print("\t***** WELCOME to \"GUESS THE NUMBER!\" *****")
    print("The number is between 1 and 50!\n")
    x = random.randint(1, 50)
    attempts = 1
    while True:
        try:
            guess = int(input("Enter a number to start playing:\n"))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if 1 <= guess <= 50:
            if guess < x:
                print("Too Low! Try Higher!\n")
                attempts += 1
            elif guess > x:
                print("Too High! Try Lower!\n")
                attempts += 1
            else:
                print(f"Congratulations! You guessed the number {x}!")
                print(f"It took you {attempts} attempts.\n")
                break
        else:
            print("Invalid Input. Enter a number between 1 and 50.\n")

def main():
    print("1. Smart Calculator")
    print("2. Guessing Game")
    choice = input("Choose option: ")
    if choice == "1":
        Smart_Calculator()
    elif choice == "2":
        guessing_game()
    else:
        print("Invalid choice")

main()