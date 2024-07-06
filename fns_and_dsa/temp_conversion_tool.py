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
            temp_input = input("Enter temperature to convert (e.g., 32F, 100C): ").strip().upper()
            
            if temp_input[-1] == 'F':
                temperature = float(temp_input[:-1])
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature} Fahrenheit is {converted_temp:.2f} Celsius.")
                break
            elif temp_input[-1] == 'C':
                temperature = float(temp_input[:-1])
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature} Celsius is {converted_temp:.2f} Fahrenheit.")
                break
            else:
                raise ValueError("Invalid temperature format. Please enter a numeric value followed by 'F' or 'C'.")
        
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()