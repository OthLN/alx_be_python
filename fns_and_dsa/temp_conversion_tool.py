FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"The temperature in Fahrenheit is: {converted_temp:.2f} °F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"The temperature in Celsius is: {converted_temp:.2f} °C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()