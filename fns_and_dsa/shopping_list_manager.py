def add_item(shopping_list, item):
    """
    Adds an item to the shopping list.

    Args:
        shopping_list (list): The current shopping list.
        item (str): The item to add.

    Returns:
        None
    """
    shopping_list.append(item)

def remove_item(shopping_list, item):
    """
    Removes an item from the shopping list.

    Args:
        shopping_list (list): The current shopping list.
        item (str): The item to remove.

    Returns:
        None
    """
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} is not in the shopping list.")

def display_list(shopping_list):
    """
    Displays the current shopping list.

    Args:
        shopping_list (list): The current shopping list.

    Returns:
        None
    """
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")

def main():
    shopping_list = []  

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == "3":
            display_list(shopping_list)
        elif choice == "4":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
