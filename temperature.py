temperature = input("Would you like to convert from Celsius or Fahrenheit? ")

if temperature == "celsius":
    celsius = int(input("Enter your temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{fahrenheit}°F")
elif temperature == "fahrenheit":
    fahrenheit = int(input("Enter your temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{celsius}°C")
else:
    print("Please choose between \"celsius\" and \"fahrenheit\"")