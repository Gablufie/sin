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

if __name__ == "__main__":
    while True:
        print("\n1. Add Todo")
        print("2. View Todos")
        print("3. Remove Todo")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item = input("Enter the task: ")
            add_todo(item)
        elif choice == "2":
            view_todos()
        elif choice == "3":
            index = int(input("Enter the index to remove: "))
            remove_todo(index - 1)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
