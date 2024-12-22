# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to iterate through each row of the pattern
while row < size:
    # Use a for loop to print asterisks (*) side by side
    for col in range(size):
        print("*", end="")
    
    # After completing each row, print a newline character
    print()
    
    # Increment the row counter
    row += 1
