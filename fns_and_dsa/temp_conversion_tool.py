FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    converted = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return converted

def convert_to_fahrenheit(celsius):
    converted = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return converted

temperature_int = int(input("Enter the temperature to convert: "))
temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower

if temperature == "f":
    print(f"{temperature_int}F is {convert_to_celsius}°C")
elif temperature == "c":
    print(f"{temperature_int}C is {convert_to_celsius}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")

