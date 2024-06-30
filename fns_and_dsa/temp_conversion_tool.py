FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        user_input = input("Enter a temperature (e.g., 68F or 20C): ")
        temperature = float(user_input[:-1])
        unit = user_input[-1].upper()

        if unit == 'F':
            celsius_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equivalent to {celsius_temp:.2f}°C.")
        elif unit == 'C':
            fahrenheit_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equivalent to {fahrenheit_temp:.2f}°F.")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'F' or 'C'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
