
import math
import equations

def main():
    print("Select operation:")
    print("add")
    print("subtract")
    print("multiply")
    print("divide")
    print("power of")

    choice = input("Enter choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'add':
        print("Result: ", equations.add(num1, num2))
    elif choice == 'subtract':
        print("Result: ", equations.subtract(num1, num2))
    elif choice == 'multiply':
        print("Result: ", equations.multiply(num1, num2))
    elif choice == 'divide':
        print("Result: ", equations.divide(num1, num2))
    elif choice == 'power of':
        print(pow(num1,num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()