#user chooses if they want to convert from celsius or fahrenheit
temperature = input("Would you like to convert from Celsius or Fahrenheit? ")

#if user chooses from celsius then they should enter their temp in celsius to convert to fahrenheit
if temperature == "celsius":
    celsius = int(input("Enter your temperature in celsius: "))
    #converts to fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    print(f"{fahrenheit}°F")

#else if the user chooses to convert from fahrenheit to celsius
elif temperature == "fahrenheit":
    fahrenheit = int(input("Enter your temperature in fahrenheit: "))
    #converts to celsius
    celsius = (fahrenheit - 32) * 5/9
    print(f"{celsius}°C")

#if they input invalid selection
else:
    print("Please choose between \"celsius\" and \"fahrenheit\"")