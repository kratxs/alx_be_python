# Prompt user to input a task description
Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_Bound = input("Is it time-bound? (yes/no): ").lower()

while True:
    match Priority:
        case "high":
            message = f"'{Task}' is a high priority task"
        case "medium":
            message = f"'{Task}' is a medium priority task"
        case "low":
            message = f"'{Task}' is a low priority task"
        case _:
            message = f"'{Task}' has an unspecified priority level"

    # Modify the message if time-bound
    if Time_Bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Print the final reminder
    print("\nReminder:", message)

    break  # Exit the loop after generating the reminder
