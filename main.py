from colorama import Fore

print(Fore.MAGENTA + "To-do List")
user_prompt = Fore.RESET + "Please type add, complete, remove, show or exit: \n"
todos = []
finished = []


# either a 'move' action to finished tasks, or the strike stays on list


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


while True:
    user_input = input(user_prompt)

    match user_input:
        case "add":
            todo_item = input("Add a task: ")
            todos.append(todo_item)
            print("\n" + Fore.MAGENTA + "To-do List")
            for number, list_item in enumerate(todos, 1):
                print(Fore.BLUE, number, Fore.RESET + list_item)
            print()
            continue
        case "complete":
            complete_item = input("Which task is complete?: ")
            if complete_item in todos:
                index = todos.index(complete_item)
                index = int(index)
                item = todos.pop(index)
                finished.append(item)
                item = strike(item)
                todos.insert(index, Fore.GREEN + item)
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                print()
                continue
            else:
                print(Fore.RED + "Task does not exist, please try again.\n")
                continue
        case "remove":
            remove_item = input("Remove a task: ")
            if remove_item in todos:
                todos.remove(remove_item)
                print("\n" + Fore.MAGENTA + "To-do List")
                for number, list_item in enumerate(todos, 1):
                    print(Fore.BLUE, number, Fore.RESET + list_item)
                if len(todos) == 0:
                    print(Fore.YELLOW + "No tasks.")
                print()
                continue
            else:
                print(Fore.RED + "Task does not exist, please try again.\n")
                continue
        case "show":
            if len(todos) == 0:
                print(Fore.RED + "There are no tasks.")
                print()
                continue
            print("\n" + Fore.MAGENTA + "To-do List")
            for number, list_item in enumerate(todos, 1):
                print(Fore.BLUE, number, Fore.RESET + list_item)
            if len(finished) > 0:
                finished_input = input(Fore.RESET + "\nSee finished tasks? (y/n): ")
                if finished_input == "y":
                    for number, list_item in enumerate(finished, 1):
                        print(Fore.YELLOW, number, Fore.YELLOW + list_item)
                    print()
                    continue
            print()
            continue
        case "exit":
            print(Fore.LIGHTYELLOW_EX + "Program terminated.")
            quit()
        case __:
            print(Fore.RED + "Please type a correct action.")
            print()

