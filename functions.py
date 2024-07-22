
def get_todos(filepath="files/subfiles/todos.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file_local:
        # Now we need to create a list from the previous todos from the text file
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/subfiles/todos.txt"):
    """ Write a to-do item list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
