# from cli import display_time
import functions
import PySimpleGUI as gui  # sg is the convention

# date_label = gui.Text(display_time)
label = gui.Text("Type in a to-do item:")
input_box = gui.InputText(tooltip="Enter list item", key="input_todo")  # tooltip is the hover info
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.read_todos(), key="selected_todo",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
remove_button = gui.Button("Remove")
# message_box = gui.Text()
buttons_column = [[edit_button],
                  [complete_button],
                  [remove_button]]

# layout argument expects a list, which will be a list of object instances
# items put in the inner brackets will be placed in one row
window = gui.Window("To-Do App",
                    layout=[[label], [input_box, add_button],
                            [list_box, gui.Column(buttons_column)]],
                    font=("Futura", 14))
while True:
    event_key, value = window.read()  # event returns pressed button's label
    print(event_key)
    print(value)
    match event_key:
        case "Add":
            todos = functions.read_todos()
            if value["input_todo"] != "":
                new_todo = value["input_todo"] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window["selected_todo"].update(values=todos)  # several values
        case "Edit":
            editing_item = value["selected_todo"][0]
            new_edited_item = value["input_todo"] + "\n"

            todos = functions.read_todos()
            index = todos.index(editing_item)
            todos[index] = new_edited_item
            functions.write_todos(todos)
            window["selected_todo"].update(values=todos)
        case "Remove":
            # add remove and clear functions for the finished list
            # also update listbox with finished list
            pass
        case "Complete":
            pass
        case "selected_todo":
            window["input_todo"].update(value=value["selected_todo"][0])
        case gui.WINDOW_CLOSED:
            break


window.close()
