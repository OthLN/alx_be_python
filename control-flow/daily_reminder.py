def main():
    task_description = input("Enter the task description: ")
    priority = input("Enter the task priority (high/medium/low): ")
    time_bound = input("Is the task time-bound? (yes or no): ")

    if priority == "high":
        reminder = f"High-priority task: {task_description}"
    elif priority == "medium":
        reminder = f"Medium-priority task: {task_description}"
    else:
        reminder = f"Low-priority task: {task_description}"

    if time_bound.lower() == "yes":
        reminder += " (requires immediate attention today!)"
    print(reminder)

if __name__ == "__main__":
    main()