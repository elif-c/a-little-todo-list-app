import colorama
from colorama import Fore

print(Fore.MAGENTA + "To-do List")
user_prompt = Fore.RESET + "Please type add, edit, complete, remove, show, cancel or exit: \n"
finished = []
# either a 'move' action to finished tasks, or the strike stays on list


def strike(text):
    result = ''
    for i in text:
        result = result + str(i) + '\u0336'
        result = result.strip("\n")
    return result


while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo_item = input("Add a task: ") + "\n"
            if todo_item == "cancel\n":
                continue
            else:
                with open("todos.rtf", "r") as file:
                    todos = file.readlines()
                    file.close()
                    todos.append(todo_item)
                with open("todos.rtf", "w", encoding="utf-8") as file:
                    file.writelines(todos)
                    file.close()
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    list_item = list_item.strip("\n")
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                print()
                continue
        case "edit":
            number_todo = input("*Number* of todo item to edit: ")
            if number_todo == "cancel":
                continue
            number_todo = int(number_todo)
            x = number_todo - 1
            try:
                if todos[x] in todos:
                    with open("todos.rtf", "r") as file:
                        todos = file.readlines()
                        file.close()
                    pop = todos.pop(x)
                    pop_new = input(f"Item to edit: {pop}") + "\n"
                    todos.insert(x, pop_new)
                    with open("todos.rtf", "w", encoding="utf-8") as file:
                        file.writelines(todos)  # writes list items in a joined string
                        file.close()
                    print("\n" + Fore.MAGENTA + "To-do List")
                    for number, list_item in enumerate(todos, 1):
                        list_item = list_item.strip("\n")
                        print(Fore.BLUE, number, Fore.RESET + list_item)
                    print()
                    continue
            except Exception as e:
                error = e
                print("\n" + Fore.RED + "Number not in list.")
                print()
        case "complete":
            complete_item = input("Which task is complete?: ")
            if complete_item.lower() == "cancel":
                continue
            elif (complete_item + "\n") in todos:
                with open("todos.rtf", "r") as file:
                    todos = file.readlines()
                    file.close()
                index = todos.index(complete_item + "\n")
                index = int(index)
                item = todos.pop(index)
                finished.append(item)
                item = strike(item)
                todos.insert(index, Fore.GREEN + item + "\n")
                with open("todos.rtf", "w", encoding="utf-8") as file:
                    file.writelines(todos)  # writes list items in a joined string
                    file.close()
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    list_item = list_item.strip("\n")
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                print()
                continue
            else:
                print(Fore.RED + "Task does not exist, please try again.\n")
                continue
        case "remove":
            remove_item = input("Remove a task: ")
            if remove_item == "cancel":
                continue
            elif (remove_item + "\n") in todos:
                with open("todos.rtf", "r") as file:
                    todos = file.readlines()
                    file.close()
                    todos.remove((remove_item + "\n"))
                with open("todos.rtf", "w", encoding="utf-8") as file:
                    file.writelines(todos)  # writes list items in a joined string
                    file.close()
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    list_item = list_item.strip("\n")
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                if len(todos) < 1:
                    print(Fore.YELLOW + "No tasks.")
                print()
                continue
            else:
                print(Fore.RED + "Task does not exist, please try again.\n")
                continue
        case "show" | "display":
            file = open("todos.rtf", "r")
            todos = file.readlines()
            file.close()
            if len(todos) < 1:
                print(Fore.RED + "There are no tasks.")
                print()
                continue
            print("\n" + Fore.MAGENTA + "To-do List")
            print(todos)
            for number, list_item in enumerate(todos, 1):
                list_item = list_item.strip("\n")
                print(Fore.BLUE, number, Fore.RESET + list_item)
            if len(finished) > 0:
                finished_input = input(Fore.RESET + "\nSee finished tasks? (y/n): ")
                if finished_input == "y":
                    for number, list_item in enumerate(finished, 1):
                        list_item = list_item.strip("\n")
                        print(Fore.YELLOW, number, Fore.YELLOW + list_item)
                    continue
            print()
        case "exit":
            print(Fore.LIGHTYELLOW_EX + "Program terminated.")
            break
        case "cancel":
            print(Fore.RED + "Nothing to cancel.")
        case _:
            print(Fore.RED + "Please type a correct action.")
            print()

print("Check back again ^^")
quit()