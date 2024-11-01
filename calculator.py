from colorama import Fore, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Calculator history to store past computations
history = []

# Arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def exponent(a, b):
    return pow(a, b)

def divide(a, b):
    if b == 0:
        print(Fore.RED + "Error! Division by zero")
        return None
    else:
        return a / b

def int_divide(a, b):
    if b == 0:
        print(Fore.RED + "Error! Division by zero")
        return None
    else:
        return a // b

def modulus(a, b):
    if b == 0:
        print(Fore.RED + "Error! Division by zero")
        return None
    else:
        return a % b

# Display history of calculations
def show_history():
    print(Fore.LIGHTMAGENTA_EX + "\nCalculation History:")
    if not history:
        print(Fore.RED + "No calculations done yet.")
    else:
        for entry in history:
            print(entry)

# Calculator main function
def calculator():
    while True:
        print_banner()
        print(Fore.RED + "Hi There! Welcome to Paul's Calculator Technology")
        print(Fore.GREEN + "Choose from the options below:")
        print(Fore.CYAN + "===============================================")
        print(Fore.YELLOW + "1. Add Numbers")
        print(Fore.YELLOW + "2. Subtract Numbers")
        print(Fore.YELLOW + "3. Multiply Numbers")
        print(Fore.YELLOW + "4. Raise to Exponents")
        print(Fore.YELLOW + "5. Divide Numbers")
        print(Fore.YELLOW + "6. Integer Division")
        print(Fore.YELLOW + "7. Modulus Operation")
        print(Fore.YELLOW + "8. Show Calculation History")
        print(Fore.YELLOW + "9. Exit")
        print(Fore.CYAN + "===============================================")

        choice = input(Fore.GREEN + "Enter a number from 1 to 9 to perform a computation: ")
        
        if choice == '9':
            print(Fore.RED + "Exiting calculator")
            break
        elif choice == '8':
            show_history()
            continue

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                num1 = float(input(Fore.BLUE + "Enter first number to compute: "))
                num2 = float(input(Fore.BLUE + "Enter second number to compute: "))
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter numbers only.")
                continue

            # Compute based on choice and save result to history
            result = None
            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = exponent(num1, num2)
                operation = f"{num1} ** {num2} = {result}"
            elif choice == '5':
                result = divide(num1, num2)
                if result is not None:
                    operation = f"{num1} / {num2} = {result}"
            elif choice == '6':
                result = int_divide(num1, num2)
                if result is not None:
                    operation = f"{num1} // {num2} = {result}"
            elif choice == '7':
                result = modulus(num1, num2)
                if result is not None:
                    operation = f"{num1} % {num2} = {result}"

            if result is not None:
                print(operation)
                history.append(operation)
        else:
            print(Fore.RED + "Invalid choice! Please enter a number between 1 and 9.")

def print_banner():
    banner = pyfiglet.figlet_format("Lexi's Enhanced Calculator")
    print(Fore.LIGHTBLUE_EX + banner)

if __name__ == "__main__":
    calculator()
