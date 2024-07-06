def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ").strip()

    print("\nCalculating...")

    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {num1} + {num2} = {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {num1} - {num2} = {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {num1} * {num2} = {result}.")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {num1} / {num2} = {result}.")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected. Please choose from +, -, *, /.")

if __name__ == "__main__":
    main()