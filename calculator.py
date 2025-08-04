from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# Loading animation
def loading():
    print(Fore.CYAN + "Calculating", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print()

# Main calculator function
def calculator():
    while True:
        print(Fore.LIGHTMAGENTA_EX + "\n================================")
        print(Fore.YELLOW + "   🚀  Simple Calculator  🚀")
        print(Fore.LIGHTMAGENTA_EX + "================================")
        print(Fore.GREEN + "1. ➕ Addition")
        print("2. ➖ Subtraction")
        print("3. ✖️ Multiplication")
        print("4. ➗ Division")
        print("5. ❌ Exit")
        print(Fore.LIGHTMAGENTA_EX + "================================" + Style.RESET_ALL)

        choice = input(Fore.CYAN + "Enter your choice (1-5): " + Style.RESET_ALL)

        if choice == '5':
            print(Fore.LIGHTRED_EX + "\nExiting Calculator. Goodbye! 👋")
            break

        # Taking inputs
        try:
            num1 = float(input(Fore.YELLOW + "Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(Fore.RED + "⚠️ Invalid input! Please enter numeric values.")
            continue

        # Perform operation
        loading()
        if choice == '1':
            print(Fore.CYAN + "✅ Result:", add(num1, num2))
        elif choice == '2':
            print(Fore.CYAN + "✅ Result:", subtract(num1, num2))
        elif choice == '3':
            print(Fore.CYAN + "✅ Result:", multiply(num1, num2))
        elif choice == '4':
            print(Fore.CYAN + "✅ Result:", divide(num1, num2))
        else:
            print(Fore.RED + "⚠️ Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    calculator()
