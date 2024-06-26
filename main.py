
def get_todos(filepath):
    with open(filepath, "r") as file_local:
        # Now we need to create a list from the previous todos from the text file
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos("files/subfiles/todos.txt")

        # Here we append the to-do we wrote to the list that we created around 2 lines ago
        todos.append(todo)

        # Now we open in write mode to overwrite the entire text file with the new list which is the old list +
        # the new list
        write_todos("files/subfiles/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("files/subfiles/todos.txt")

        # new_todos = []
        #
        # for item in todos:
        #     new_item = item.strip().title()
        #     new_todos.append(new_item)

        # new_todos = [item.strip().title() for item in todos]

        print(f"Todos left to complete - {len(todos)}")
        for index, item in enumerate(todos):
            item = item.strip().title()
            index += 1
            print(f"{index}-{item}")
        # print(f"Todos completed - {len(completed_todos)}")
        # for index, item in enumerate(completed_todos):
        #     item = item.title()
        #     index += 1
        #     print(f"{index}-{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("files/subfiles/todos.txt")
            # print("Here is existing todos", todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            # print("Here is how it will be", todos)

            write_todos("files/subfiles/todos.txt", todos)
        except ValueError:
            print("Sorry but we are expecting the todo number rather than the todo name :/")
            continue

    elif user_action.startswith("completed"):
        try:
            completed = int(user_action[10:])
            completed -= 1

            todos = get_todos("files/subfiles/todos.txt")

            todo_to_remove = todos[completed].strip()
            todos.pop(completed)

            write_todos("files/subfiles/todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Sorry the number that you entered does not exist on the list")
            continue
        except ValueError:
            print("Sorry only numbers are allowed :/")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered an unknown command :(")

print("Bye!")
