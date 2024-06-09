
todos = []
completed_todos = []

while True:
    user_action = input("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            print(f"Todos left to complete - {len(todos)}")
            for index, item in enumerate(todos):
                item = item.title()
                index += 1
                print(f"{index}-{item}")
            print(f"Todos completed - {len(completed_todos)}")
            for index, item in enumerate(completed_todos):
                item = item.title()
                index += 1
                print(f"{index}-{item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "completed":
            completed = int(input("Enter the number of the completed todo: "))
            completed -= 1
            completed_todos.append(todos.pop(completed))
        case "exit":
            break
        case _:
            print("Hey, you entered an unknown command :(")

print("Bye!")
