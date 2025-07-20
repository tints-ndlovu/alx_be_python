task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower
time_bound = input("Is it time-bound? (yes/no): ").lower


match priority:
    case "high":
        message = print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        message = print(f"Reminder: '{task}' is a MEDIUM priority task.")
    case "low":
        message = print(f"Reminder: '{task}' is a LOW priority task.")
    case _:
        message = print(f"Reminder: '{task}' has an UNKNOWN priority level.")

if time_bound == "yes":
    message += " This task requires immediate attention today!"


print("\n" + message)
