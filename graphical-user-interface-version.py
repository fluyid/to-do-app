import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple5")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
                      values=functions.get_todos(),
                      key="todo_items",
                      enable_events=True,
                      size=(45, 10))
# 45 characters wide and 10 characters high

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To Do App",
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(
        value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, event)
    # print(2, values)
    # print(3, values['todo_items'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todo_items'][0]
                # we add 0 because values['todo_items'] gives us a list with a single item
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                # .index gives us the index of a particular object
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todo_items'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",
                         font=("Helvetica", 12))
        case "Complete":
            try:
                todo_to_complete = values['todo_items'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo_items'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first",
                         font=("Helvetica", 12))
        case "Exit":
            break
        case 'todo_items':
            window['todo'].update(value=values['todo_items'][0])
        case sg.WIN_CLOSED:
            break

window.close()
