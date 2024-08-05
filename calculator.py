from colorama import Fore, Back, Style, init
import pyfiglet

init(autoreset = True)

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def exponent(a, b):
    return pow(a,b)

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

def calculator():
    while True:
        print_banner()
        print(Fore. RED + "Hi There! Welcome to Lexi's latest Calculator Technology")
        print(Fore. GREEN + "Choose from the options below:")
        print(Fore.CYAN +" ==============================================")
        print(Fore.YELLOW + "1. Add Numbers:")
        print(Fore.YELLOW + "2. Subtract Numbers:")
        print(Fore.YELLOW + "3. Multiply Numbers:")
        print(Fore.YELLOW + "4. Raise to Exponents:")
        print(Fore.YELLOW + "5. Divide Numbers:")
        print(Fore.YELLOW + "6. Integer Division")
        print(Fore.YELLOW+ "7. Exit")
        print(Fore.CYAN + "==============================================")
        
        choice = input(Fore. GREEN + "Enter number from 1 to 6 to perform computation: ")
        if choice == '7':
            print(Fore.RED + "Exiting calculator")
            break
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input(Fore.BLUE + "Enter first number to compute: "))
                num2 = float(input(Fore.BLUE + "Enter second number to compute: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {substract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} ** {num2} = {exponent(num1, num2)}")
            elif choice == '5':
                result = divide(num1, num2)
                if result is not None:
                    print(f"{num1} / {num2} = {result}")
            elif choice == '6':
                result = int_divide(num1, num2)
                if result is not None:
                    print(f"{num1} // {num2} = {result}")
        else:
            print(Fore.RED + "Invalid choice! Please enter a number between 1 and 7.")

def print_banner():
    banner = pyfiglet.figlet_format("Lexi's Calculator")
    print(Fore.LIGHTBLUE_EX + banner)

if __name__ == "__main__":
    calculator()
