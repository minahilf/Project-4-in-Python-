def fahrenheit_to_celsius():
  far = float(input("Enter Tempreture in Farenheit: "))
  degrees_celsius = (far - 32) * 5.0/9.0
  print(f"The Tempreture in Fahrenheit {far}F is {degrees_celsius}C")
fahrenheit_to_celsius()