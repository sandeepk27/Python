user_value = input("Enter a temperature in Fahrenheit to convert to Celsius ")
fahrenheit_temp = float(user_value)
celsius_temp = (fahrenheit_temp - 32) * (5/9)
print(fahrenheit_temp, "in Celsius is", celsius_temp)