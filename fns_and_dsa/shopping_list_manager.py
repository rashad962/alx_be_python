def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to manage the shopping list
def main():
    shopping_list = []  # Initialize the empty shopping list
    
    while True:
        display_menu()  # Show the menu
        try:
            choice = int(input("Enter your choice: "))  # Get user's choice as an integer
            
            # Validate input choice
            if choice < 1 or choice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
            
            if choice == 1:  # Add an item to the list
                item = input("Enter the item to add: ")
                shopping_list.append(item)  # Add item to the list
                print(f"'{item}' has been added to your shopping list.")
            
            elif choice == 2:  # Remove an item from the list
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)  # Remove item from the list
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' not found in your shopping list.")
            
            elif choice == 3:  # View the current shopping list
                if shopping_list:
                    print("\nCurrent Shopping List:")
                    for item in shopping_list:
                        print(f"- {item}")
                else:
                    print("Your shopping list is empty.")
            
            elif choice == 4:  # Exit the program
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the program if it's the main script
if __name__ == "__main__":
    main()
