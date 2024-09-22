# Write a python program using function to convert Celsius to Fahrenheit.
def convert_celsius2farenheit(cel):
    far = (cel*1.8) + 32
    return far

celcius = int(input("Enter temperature in Celsius: "))

print(f"The temperature in Farenheit is: {convert_celsius2farenheit(celcius)}")