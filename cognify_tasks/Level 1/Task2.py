
print("Temperature Conversion 'Task 2' -Level 1")
print("-----------------------------------------")
temp = float(input("Enter the temperature value: "))
unit = input("enter the unit('C' for celcius or 'F' for fahrenheit): ").upper()

if unit == 'C':
    celcius = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {celcius:.2f}°C celcius")
elif unit == 'F':
    Fahrenheit = (temp * 9/35) +32
    print(f"{temp}°C is equal to {Fahrenheit:.2f}F Fahrenheit")
else:
    print("invalid unit enter 'C' for Celcius or 'F' for fahrenheit")

#OUTPUT
'''Temperature Conversion 'Task 2' -Level 1
-----------------------------------------
Enter the temperature value: 234
enter the unit('C' for celcius or 'F' for fahrenheit): f
234.0°C is equal to 92.17F Fahrenheit'''     

