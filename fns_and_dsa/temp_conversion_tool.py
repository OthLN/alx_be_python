FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    while True:
        try:
            temp_input = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            
            if unit == 'F':
                converted_temp = convert_to_celsius(temp_input)
                print(f"{temp_input:.1f}°F is {converted_temp:.2f}°C")
                break
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temp_input)
                print(f"{temp_input:.1f}°C is {converted_temp:.2f}°F")
                break
            else:
                raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
        
        except ValueError as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()