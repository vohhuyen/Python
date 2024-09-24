def display_todos(todos):
    print("\nTodo list:")
    if not todos:
        print("No tasks!")
    else:
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")

def main():
    todos = []
    
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        match choice:
            case '1':
                todo = input("Enter a task to add: ")
                todos.append(todo) 
                print(f"Task added: {todo}")

            case '2':
                display_todos(todos) 

            case '3':
                display_todos(todos)
                index = int(input("Enter the number of the task to delete: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index) 
                    print(f"Task deleted: {removed}")
                else:
                    print("Invalid task number!")

            case '4':
                print("Thank you for using the Todo List app!")
                break

            case _:
                print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
