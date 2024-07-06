FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp = float(input("Enter a temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

    if unit.upper() == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"The temperature in Fahrenheit is: {converted_temp}")
    elif unit.upper() == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"The temperature in Celsius is: {converted_temp}")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

except ValueError as e:
    print(e)