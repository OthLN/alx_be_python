def main():
    task = input("Enter the task description: ")

    priority = input("Enter the priority level (high, medium, low): ").strip().lower()

    time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

    print("\nReminder:")
    
    match priority:
        case 'high':
            reminder = f"{task} (Priority: High)"
        case 'medium':
            reminder = f"{task} (Priority: Medium)"
        case 'low':
            reminder = f"{task} (Priority: Low)"
        case _:
            print("Invalid priority level entered.")
            return
    
    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"

    print(reminder)

if __name__ == "__main__":
    main()