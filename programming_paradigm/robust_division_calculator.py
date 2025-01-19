import sys

def safe_divide(numerator, denominator):
    try:
        # Convert the numerator and denominator to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division and return the result
        return f"The result of the division is {numerator / denominator}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

def main():
    # Check if there are exactly two command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python robust_division_calculator.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function with user inputs
    result = safe_divide(numerator, denominator)

    # Print the result of the division or the error message
    print(result)

if __name__ == "__main__":
    main()
