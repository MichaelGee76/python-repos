def main():
  error_message = "Invalid input. Try again."
  temp_unit = input("Fahrenheit or Celsius? Type C or F ").lower()
  if temp_unit != "c" and temp_unit != "f":
    print(error_message)
    return
  
  temperature = input("What temperature? ")
  try:
    temperature = int(temperature)
  except ValueError:
    print(error_message)  
    return
  
  result = convert_temp(temp_unit, temperature)
  print("The temperature: ",result )

def convert_temp(unit, temp):
  if unit == "c":
    fahrenheit_to_celsius = (temp - 32) * (5/9)
    return f"{round(fahrenheit_to_celsius, 2)}°C"
  else:
    celsius_to_fahrenheit = (temp * 9/5) + 32
    return f"{round(celsius_to_fahrenheit, 2)}°F"
  
  
main()  