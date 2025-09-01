# Importing the 'json' module to read and write JSON files
# JSON stands for JavaScript Object Notation and is used to store data in key-value format (like Python dictionaries)
import json

# This is the name of the JSON file where all the tasks will be saved and loaded from
file_name = "todo_list.json"

# This function loads existing tasks from the JSON file
def load_tasks():
    try:
        # Open the file in 'read' mode
        with open(file_name, "r") as file:
            # Load the JSON data (convert JSON string into Python dictionary)
            return json.load(file)
    except:
        # If file doesn't exist or there's an error, return an empty task list in dictionary format
        return {"tasks": []}

# This function saves the current task list to the JSON file
def save_tasks(tasks):
    try:
        # Open the file in 'write' mode, which overwrites the previous content
        with open(file_name, "w") as file:
            # Convert Python dictionary to JSON and save it into the file
            json.dump(tasks, file)
    except:
        # If saving fails, print an error message
        print("Failed to save.")

# This function displays all the tasks
def view_tasks(tasks):
    print()  # Just prints a blank line for better formatting
    task_list = tasks["tasks"]  # Extract the list of tasks from the dictionary
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List:")
        # Loop through each task and show its index, description, and status
        for idx, task in enumerate(task_list):
            # If task is completed, show [Completed], else show [Pending]
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

# This function lets the user add a new task
def create_task(tasks):
    # Ask user to enter task description
    description = input("Enter the task description: ").strip()
    if description:
        # Add a new task with default 'complete' status as False
        tasks["tasks"].append({"description": description, "complete": False})
        # Save the updated list to file
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")

# This function lets the user mark a task as complete
def mark_task_complete(tasks):
    # First, show the current tasks so user can choose
    view_tasks(tasks)
    try:
        # Ask the user which task number they want to mark as complete
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        # Check if the number is valid (within range)
        if 1 <= task_number <= len(tasks["tasks"]):
            # Update the task's 'complete' status to True
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)  # Save the updated list
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

# This is the main function that controls the program's menu and flow
def main():
    # Load existing tasks from the file
    tasks = load_tasks()

    # Infinite loop to keep showing the menu until user exits
    while True:
        print("\nTo-Do List Manager")  # Title of the app
        print("1. View Tasks")        # Option 1
        print("2. Add Task")          # Option 2
        print("3. Complete Task")     # Option 3
        print("4. Exit")              # Option 4

        # Ask the user to choose an option
        choice = input("Enter your choice: ").strip()

        # Perform actions based on user's choice
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye")  # Exit message
            break  # Breaks out of the while loop, ending the program
        else:
            print("Invalid choice. Please try again.")  # If input is not 1-4

# Run the main function to start the program
main()