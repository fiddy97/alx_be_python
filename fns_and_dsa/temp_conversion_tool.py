# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Used to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Used to convert Celsius to Fahrenheit
FREEZING_POINT = 32  # Freezing point of water in Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT
    return fahrenheit

# Main function to interact with the user
def main():
    try:
        # Ask the user for the temperature and unit
        temperature = float(input("Enter the temperature: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        # Convert the temperature based on the unit
        if unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result:.2f}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")

# Run the program
if __name__ == "__main__":
    main()