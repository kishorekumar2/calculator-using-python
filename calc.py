def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")

            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid Input")

        # Check if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
