def temp_conversion_tool():
  """Converts temperatures between Celsius and Fahrenheit."""

  # Define global conversion factors
  FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
  CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

  def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius.

    Args:
      fahrenheit: The temperature in Fahrenheit.

    Returns:
      The temperature in Celsius.
    """

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

  def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit.

    Args:
      celsius: The temperature in Celsius.

    Returns:
      The temperature in Fahrenheit.
    """

    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

  # Get user input
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
      break
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

  # Convert temperature based on user input
  if unit == "C":
    converted_temperature = convert_to_fahrenheit(temperature)
    unit = "F"
  elif unit == "F":
    converted_temperature = convert_to_celsius(temperature)
    unit = "C"
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")
    return

  # Display the converted temperature
  print(f"{temperature:.1f}°{unit} is {converted_temperature:.1f}°C")

# Call the function only if the script is executed directly
if __name__ == "__main__":
  temp_conversion_tool()
