import hw8_temperature

def hw8_main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        
        converted_to_fahrenheit = temperature.celsius_to_fahrenheit(celsius)
        converted_to_celsius = temperature.fahrenheit_to_celsius(fahrenheit)

        print(f"{celsius}°C is {converted_to_fahrenheit:.2f}°F")
        print(f"{fahrenheit}°F is {converted_to_celsius:.2f}°C")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__hw8_main__":
    hw8_main()