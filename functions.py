def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius *9/5+32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) *5/9
    return celsius


user_choice = str(input("Please enter C or F : "))
if user_choice.lower() == 'c':
    temperature = float(input("Please enter the temperature: "))
    print(celsius_to_fahrenheit(temperature))

if user_choice.lower() == 'f':
    temperature = float(input("Please enter the temperature: "))
    print(fahrenheit_to_celsius(temperature))