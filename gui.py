# from cli import display_time
import functions
import PySimpleGUI as gui  # sg is the convention

# date_label = gui.Text(functions.display_time())
label = gui.Text("Type in a to-do item:")
input_box = gui.InputText(tooltip="Enter list item", key="input_todo")  # tooltip is the hover info
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.read_todos(), key="selected_todo",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
remove_button = gui.Button("Remove")
see_finished = gui.Button("See Finished Tasks", key="see_finished")

buttons_column = [[edit_button],
                  [complete_button],
                  [remove_button]]
layout = [[label],
          [input_box, add_button],
          [list_box, gui.Column(buttons_column)],
          [see_finished]]

finished_label = gui.Text("Finished Tasks", text_color="purple4")
finished_item = gui.Input(key="chosen_finished")
remove_finished_button = gui.Button("Remove", key="rm_finished")
clear_button = gui.Button("Clear")
go_back_button = gui.Button("Go Back")
finished_box = gui.Listbox(values=functions.read_todos("finished_todos.rtf"),
                           key="finished_todo", enable_events=True,
                           size=[45, 10])
finished_layout = [[finished_label],
                   [finished_item, remove_finished_button],
                   [finished_box, clear_button],
                   [go_back_button]]

# layout argument expects a list, which will be a list of object instances
# items put in the inner brackets will be placed in one row
window = gui.Window("To-Do App",
                    layout=layout,
                    font=("Futura", 14))
finished_window = gui.Window("To-Do App",
                             layout=finished_layout,
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
                window.refresh()
                functions.write_todos(todos)
                window.refresh()
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
            removing_item = value["selected_todo"][0]
            todos = functions.read_todos()
            index = todos.index(removing_item)
            todos.pop(index)
            window.refresh()
            functions.write_todos(todos)
            window["selected_todo"].update(values=todos)
            # add remove and clear functions for the finished list
            # also update listbox with finished list
        case "Complete":
            complete_item = value["selected_todo"][0]
            todos = functions.read_todos()
            index = todos.index(complete_item)
            item = todos.pop(index)
            window.refresh()
            functions.write_todos(todos)
            finished = functions.read_todos("finished_todos.rtf")
            finished.append(item)
            window.refresh()
            functions.write_todos(finished, "finished_todos.rtf")
            window["selected_todo"].update(values=todos)
        case "see_finished":
            window.refresh(layout=finished_layout)  # TypeError: 'str' object cannot be interpreted as an integer
        case "Go Back":
            window.update(layout=layout)  # TypeError: 'str' object cannot be interpreted as an integer
        case "selected_todo":
            window["input_todo"].update(value=value["selected_todo"][0])
        case "finished_todo":
            pass
            # window["chosen_finished"].update(value=value["finished_todo"][0])
        case gui.WINDOW_CLOSED:
            break


window.close()
