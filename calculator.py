def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input("Enter an operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        
        another = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
