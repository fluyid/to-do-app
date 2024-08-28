FILEPATH = "files/subfiles/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file_local:
        # Now we need to create a list from the previous todos from the text file
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do item list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    # the current py file has the value of __main__ for __name__
    # the current py file will have the value of functions for __name__ when opened in another py file
    print("Hello")
    print(get_todos())
