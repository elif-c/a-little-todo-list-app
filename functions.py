import colorama
from colorama import Fore


def read_todos(filepath="todos.rtf"):
    """ Read the todo list items file and return the contents as a list."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.rtf"):
    """ Write the modified todos list in the program onto the file specified."""
    with open(filepath, "w", encoding="utf-8") as file_local:
        file_local.writelines(todos_arg)
        # no need to return anything


def enumerate_todos(todos_list_arg, color=Fore.BLUE):
    for number, list_item in enumerate(todos_list_arg, 1):
        list_item = list_item.strip("\n")
        print(color, number, Fore.RESET + list_item)
