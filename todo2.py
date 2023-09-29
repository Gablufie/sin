# todo.py

todos = []

def add_todo(item):
    todos.append({"task": item, "complete": False})

def view_todos():
    for idx, item in enumerate(todos):
        status = "Done" if item["complete"] else "Not Done"
        print(f"{idx + 1}. {item['task']} - {status}")

def mark_as_complete(index):
    if 0 <= index < len(todos):
        todos[index]["complete"] = True
    else:
        print("Invalid index!")

def remove_todo(index):
    if 0 <= index < len(todos):
        removed_item = todos.pop(index)
        print(f"Removed: {removed_item['task']}")
    else:
        print("Invalid index!")

def edit_todo(index, new_description):
    if 0 <= index < len(todos):
        todos[index]["task"] = new_description
        print("Task updated successfully!")
    else:
        print("Invalid index!")

def view_completed_todos():
    completed_todos = [item for item in todos if item["complete"]]
    if completed_todos:
        print("\nCompleted Todos:")
        for idx, item in enumerate(completed_todos):
            print(f"{idx + 1}. {item['task']}")
    else:
        print("\nNo completed todos.")

if __name__ == "__main__":
    while True:
        print("\n1. Add Todo")
        print("2. View Todos")
        print("3. Mark as Complete")
        print("4. Edit Todo")
        print("5. Remove Todo")
        print("6. View Completed Todos")
        print("7. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item = input("Enter the task: ")
            add_todo(item)
        elif choice == "2":
            view_todos()
        elif choice == "3":
            index = int(input("Enter the index to mark as complete: "))
            mark_as_complete(index - 1)
        elif choice == "4":
            index = int(input("Enter the index of the task to edit: "))
            new_description = input("Enter the new task description: ")
            edit_todo(index - 1, new_description)
        elif choice == "5":
            index = int(input("Enter the index to remove: "))
            remove_todo(index - 1)
        elif choice == "6":
            view_completed_todos()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")
