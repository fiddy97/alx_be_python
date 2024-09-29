# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_CELSIUS = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FREEZING_POINT_CELSIUS
    celsius = (fahrenheit - FREEZING_POINT_CELSIUS) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FREEZING_POINT_CELSIUS
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_CELSIUS
    return fahrenheit

# Input validation function
def get_temperature_input():
    try:
        temp = float(input("Enter the temperature to convert: "))
        return temp
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_temperature_unit():
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return unit

# Main function to handle user interaction
def main():
    try:
        temp = get_temperature_input()
        unit = get_temperature_unit()

        if unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main() 