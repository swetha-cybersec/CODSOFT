def calculate(num1, num2, operation):
    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        return num1 / num2
    else:
        return "Invalid operation"

def main():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice (1/2/3/4): ")

    if operation not in ["1", "2", "3", "4"]:
        print("Invalid operation choice.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "4" and num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    result = calculate(num1, num2, operation)
    print("The result is:", {result})

if __name__ == "__main__":
    main()
