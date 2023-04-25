# from cli import display_time
import functions
import PySimpleGUI as gui

# date_label = gui.Text(display_time)
label = gui.Text("Type in a to-do item:")
input_box = gui.InputText(tooltip="Enter list item")  # tooltip is the hover information
add_button = gui.Button("Add")

# layout argument expects a list, which will be a list of object instances
# items put in the inner brackets will be placed in one row
window = gui.Window("To-Do App", layout=[[label, input_box, add_button]])
window.read()
window.close()
