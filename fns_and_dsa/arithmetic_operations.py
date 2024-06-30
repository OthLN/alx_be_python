def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        num1 (float): First operand.
        num2 (float): Second operand.
        operation (str): Arithmetic operation ('add', 'subtract', 'multiply', or 'divide').

    Returns:
        float: Result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operation"

if __name__ == "__main__":
    result = perform_operation(10, 5, 'divide')
    print(f"Result: {result}")
