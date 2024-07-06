def main():
    task = input("Enter your task: ")

    priority = input("Priority (high/medium/low): ").strip().lower()

    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"Reminder:\n'{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder:\n'{task}' is a high priority task.")
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder:\n'{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder:\n'{task}' is a medium priority task.")
        case 'low':
            if time_bound == 'yes':
                print(f"Reminder:\n'{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Reminder:\n'{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level entered.")

if __name__ == "__main__":
    main()