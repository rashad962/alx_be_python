def temp_conversion_tool():
  """Converts temperatures between Celsius and Fahrenheit."""

  # Checks for Definition of global conversion factors
  FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
  CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

  # Checks for Implement conversion functions
  def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

  def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

  # Checks for User interaction
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      # Checks for Implementation of Value Error
      if unit not in ("C", "F"):
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
      break
    except ValueError as e:
      print(e)

  if unit == "C":
    converted_temperature = convert_to_fahrenheit(temperature)
    converted_unit = "F"
  elif unit == "F":
    converted_temperature = convert_to_celsius(temperature)
    converted_unit = "C"

  print(f"{temperature:.1f}°{unit} is {converted_temperature:.1f}°{converted_unit}")

if __name__ == "__main__":
  temp_conversion_tool()
