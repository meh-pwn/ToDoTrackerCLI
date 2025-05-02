import json
filename = "users_task.json"


def check_file(filename):
    """The function checks if a file exists in a directory and creates it otherwise."""
    try:
        with open(filename, 'x'):
            pass
    except FileExistsError:
        pass


def add_task(data):
    """Function adds a new task to our dictionary."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except:
            id = 1
            tasks_dict[id] = data
        else:
            id = len(tasks_dict) + 1
            tasks_dict[id] = data

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)


def main():
    """Main function."""
    check_file(filename)
    users_input = input()
    pos = users_input.find(" ")
    command, description = users_input[:pos], users_input[pos + 1:len(users_input)]

    print(command)
    print(description)
    
    match command.lower():
        case "add":
            add_task(description)
        case "delete":
            pass
        case "update":
            pass

if __name__ == "__main__":
    while True:
        main()