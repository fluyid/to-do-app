import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
                      values=functions.get_todos(),
                      key="todo_items",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("To Do App",
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button]
                   ],
                   font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo_items'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todo_items'][0]
            # we add 0 because values['todo_items'] gives us a list with a single item
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            # .index gives us the index of a particular object
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
        case 'todo_items':
            window['todo'].update(value=values['todo_items'][0])
        case sg.WIN_CLOSED:
            break

window.close()
