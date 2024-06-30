task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")
if priority == "high":
    reminder = f"High-priority task: {task}"
elif priority == "medium":
    reminder = f"Medium-priority task: {task}"
else:
    reminder = f"Low-priority task: {task}"

if time_bound.lower() == "yes":
    reminder += " (requires immediate attention today!)"
print(reminder)