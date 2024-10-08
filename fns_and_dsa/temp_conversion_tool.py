FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) +32

def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        convert_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}C is {convert_temp}F")
    elif unit == 'F':
        convert_temp = convert_to_celsius(temperature)
        print(f"{temperature}F is {convert_temp}C")
    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()