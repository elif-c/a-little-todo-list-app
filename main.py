import colorama
from colorama import Fore

print(Fore.MAGENTA + "To-do List")
user_prompt = Fore.RESET + "Please type add, edit, complete, remove, show, cancel or exit: \n"

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip().lower()

    if user_input.startswith("add"):
        todo_item = user_input[4:]
        if len(todo_item) < 1:
            print("\n" + Fore.RED + "Please enter a task.")
            continue
        with open("todos.rtf", "r") as file:
            todos = file.readlines()
        todos.append(todo_item + "\n")
        with open("todos.rtf", "w", encoding="utf-8") as file:
            file.writelines(todos)
        print("\n" + Fore.MAGENTA + "To-do List")
        for number, list_item in enumerate(todos, 1):
            list_item = list_item.strip("\n")
            print(Fore.BLUE, number, Fore.RESET + list_item)
        print()
        todo_item = todo_item.strip("\n")
        message = f"{todo_item} is added to tasks."
        print(message)
        print()
        continue
    elif user_input.startswith("edit"):
        try:
            number_todo = input("*Number* of todo task to edit: ")
            if number_todo.lower() == "cancel":
                print(Fore.RED + "Canceled")
                continue
            number_todo = int(number_todo) - 1
        except ValueError:
            print("\n" + Fore.RED + "Please enter *number* of task.")
            print()
            continue
        try:
            with open("todos.rtf", "r") as file:
                todos = file.readlines()
            if todos[number_todo] in todos:
                pop = todos.pop(number_todo)
                pop_new = input(f"Enter new task: {pop}") + "\n"
                if pop_new.lower() == "cancel\n":
                    print(Fore.RED + "Canceled")
                    continue
                todos.insert(number_todo, pop_new)
                with open("todos.rtf", "w", encoding="utf-8") as file:
                    file.writelines(todos)
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    list_item = list_item.strip("\n")
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                print()
                pop = pop.strip("\n")
                pop_new = pop_new.strip("\n")
                message = f"{pop} is edited into {pop_new}."
                print(message)
                print()
                continue
        except IndexError:
            print("\n" + Fore.RED + "Number not in list, please try again.")
            print()
            continue
    elif user_input.startswith("complete"):
        try:
            complete_item = input("*Number* of task to mark as complete?: ")
            if complete_item.lower() == "cancel":
                print(Fore.RED + "Canceled")
                continue
            complete_item = int(complete_item) - 1
        except ValueError:
            print("\n" + Fore.RED + "Please enter *number* of task.")
            print()
            continue
        with open("todos.rtf", "r") as file:
            todos = file.readlines()
        try:
            if todos[complete_item] in todos:
                item = todos.pop(complete_item)
                with open("finished_todos.rtf", "r") as file:
                    finished = file.readlines()
                finished.append(item + "\n")
                with open("finished_todos.rtf", "w") as file:
                    file.writelines(finished)
                with open("todos.rtf", "w", encoding="utf-8") as file:
                    file.writelines(todos)
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    list_item = list_item.strip("\n")
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                print()
                item = item.strip("\n")
                message = f"{item} is completed and moved to finished tasks."
                print(Fore.RESET + message)
                print()
                continue
        except IndexError:
            print("\n" + Fore.RED + "Task does not exist, please try again.\n")
            continue
    elif user_input.startswith("remove"):
        try:
            remove_item = input("*Number* of task to remove: ")
            if remove_item.lower() == "cancel":
                continue
            remove_item = int(remove_item) - 1
        except ValueError:
            print("\n" + Fore.RED + "Please enter *number* of task.")
            print()
            continue
        with open("todos.rtf", "r") as file:
            todos = file.readlines()
        try:
            if todos[remove_item] in todos:
                removed_item = todos.pop(remove_item)
                with open("todos.rtf", "w", encoding="utf-8") as file:
                    file.writelines(todos)
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    list_item = list_item.strip("\n")
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                if len(todos) < 1:
                    print(Fore.YELLOW + "No tasks.")
                removed_item = removed_item.strip("\n")
                message = Fore.RESET + f"{removed_item} is removed from tasks."
                print(message)
                print()
                continue
        except IndexError:
            print("\n" + Fore.RED + "Task does not exist, please try again.\n")
            continue
    elif user_input.startswith("show") or user_input.startswith("display"):
        with open("todos.rtf", "r") as file:
            todos = file.readlines()
        if len(todos) < 1:
            print(Fore.RED + "There are no tasks.")
            print()
            continue
        print("\n" + Fore.MAGENTA + "To-do List")
        # print(todos) to see list items with end lines
        for number, list_item in enumerate(todos, 1):
            list_item = list_item.strip("\n")
            print(Fore.BLUE, number, Fore.RESET + list_item)
        with open("finished_todos.rtf", "r") as file:
            finished = file.readlines()
        if len(finished) > 0:
            finished_user_input = input(Fore.RESET + "\nSee finished tasks? (y/n): ")
            if finished_user_input.lower() == "y":
                for number, list_item in enumerate(finished, 1):
                    list_item = list_item.strip("\n")
                    print(Fore.YELLOW, number, Fore.YELLOW + list_item)
                clear_input = input("Would you like to clear finished tasks? (y/n): ")
                if clear_input.lower() == "y":
                    sure = input("Are you sure? (y/n): ")
                    if sure.lower() == "y":
                        with open("finished_todos.rtf", "r") as file:
                            finished = file.readlines()
                        finished.clear()
                        with open("finished_todos.rtf", "w") as file:
                            file.writelines(finished)
                        print(Fore.YELLOW + "Finished tasks are cleared.")
        print()
    elif user_input.startswith("exit"):
        print(Fore.LIGHTYELLOW_EX + "Program terminated.")
        break
    elif user_input.startswith("cancel"):
        print("\n" + Fore.RED + "Nothing to cancel.")
    else:
        print("\n" + Fore.RED + "Please type a correct action.")
        print()

print("Check back again ^^")
quit()
