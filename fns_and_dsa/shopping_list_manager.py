shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"Item '{item}' added to the shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item '{item}' removed from the shopping list.")
    else:
        print(f"Item '{item}' not found in the shopping list.")

def view_list():
    print("Current Shopping List:")
    for item in shopping_list:
        print(item)
    print()

def display_menu():
    print("Shopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ").strip()
    return choice

def main():
    while True:
        choice = display_menu()

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()