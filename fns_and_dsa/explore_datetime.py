from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date by adding the specified number of days
    future_date = datetime.now() + timedelta(days=days_to_add)
    
    # Print the future date in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Main function to execute the tasks
if __name__ == "__main__":
    display_current_datetime()  # Display the current date and time
    calculate_future_date()     # Calculate and display the future date
