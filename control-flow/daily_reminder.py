# Prompt user to input a task description
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower
time_bound = input("Is it time bound? (yes/no): ").lower

while True:
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unspecified priority level"

    # Modify the message if time-bound
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Print the final reminder
    print("\nReminder:", message)

    break  # Exit the loop after generating the reminder
