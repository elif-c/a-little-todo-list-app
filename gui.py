# from cli import display_time
import functions
import PySimpleGUI as gui

# date_label = gui.Text(display_time)
label = gui.Text("Type in a to-do item:")
input_box = gui.InputText(tooltip="Enter list item", key="added_todo")  # tooltip is the hover info
add_button = gui.Button("Add")

# layout argument expects a list, which will be a list of object instances
# items put in the inner brackets will be placed in one row
window = gui.Window("To-Do App",
                    layout=[[label], [input_box, add_button]],
                    font=("Futura", 14))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = value["added_todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WINDOW_CLOSED:
            break


window.close()
