import json
from datetime import datetime
filename = "users_task.json"


def check_file(filename):
    """The function checks if a file exists in a directory and creates it otherwise."""
    try:
        with open(filename, 'x'):
            pass
    except FileExistsError:
        pass


def crush_program(reason):
    """The function terminates the program when an error occurs."""
    raise SystemExit(f"Error: {reason}")
    

def parse_input(users_input):
    """The function splits a string into parts, taking into account spaces and quotation marks."""
    parts = []
    current_part = []
    in_quotes = False

    for char in users_input:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ' ':
            if in_quotes == False:
                parts.append(''.join(current_part))
                current_part = []
            elif in_quotes == True:
                current_part.append(char)
        else:
            current_part.append(char)
    
    if current_part:
        parts.append(''.join(current_part))
        current_part = []
 
    return parts


def add_task(data):
    """The function adds a new task to our dictionary."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            id = 1
            created_at = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            tasks_dict[id] = [data, "todo", created_at, " "]
        else:
            id = len(tasks_dict) + 1
            created_at = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            tasks_dict[id] = [data, "todo", created_at, " "]

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)


def delete_task(id):
    """The function delete a task to our dictionary."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            crush_program("You can't delete the task because the to-do list is empty now.")
        else:
            if id in tasks_dict.keys():
                key_exists = True
            else:
                key_exists = False
            
            if key_exists:
                tasks_dict.pop(id)
            else:
                crush_program("You can't delete this task because it's not on the to-do list.")

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)


def update_task(id, data):
    """The function update a current task to our dictionary."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            crush_program("You can't update the task because the to-do list is empty now.")
        else:
            if id in tasks_dict.keys():
                key_exists = True
            else:
                key_exists = False
            
            if key_exists:
                status = tasks_dict[id][1]
                created_at = tasks_dict[id][2]
                updated_at = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                tasks_dict[id] = [data, status, created_at, updated_at]
            else:
                crush_program("You can't update this task because it's not on the to-do list.")

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)


def update_status(id, status):
    """The function update a current status for task to our dictionary."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            crush_program("You can't mark this task because the to-do list is empty now.")
        else:
            if id in tasks_dict.keys():
                key_exists = True
            else:
                key_exists = False
            
            if key_exists:
                tasks_dict[id][1] = status
            else:
                 crush_program("You can't mark this task because it's not on the to-do list.")
    
    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)


def show_full_list():
    """The function displays a list of all tasks."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            crush_program("You can't see this list because the to-do list is empty now.")
        else:
            for key, value in tasks_dict.items():
                print(key, value[0], value[1], value[2], value[3])


def show_done_list():
    """The function displays a list of done tasks."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            crush_program("You can't see this list because the to-do list is empty now.")
        else:
            found = False
            for key, value in ((k, v) for k, v in tasks_dict.items() if v[1] == "done"):
                print(key, value[0], value[1], value[2], value[3])
                found = True
            
            if found == False:
                print("Nothing to display.")


def show_progress_list():
    """The function displays a list of in-progress tasks."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            crush_program("You can't see this list because the to-do list is empty now.")
        else:
            found = False
            for key, value in ((k, v) for k, v in tasks_dict.items() if v[1] == "in-progress"):
                print(key, value[0], value[1], value[2], value[3])
                found = True
            
            if found == False:
                print("Nothing to display.")


def show_todo_list():
    """The function displays a list of todo tasks."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            crush_program("You can't see this list because the to-do list is empty now.")
        else:
            found = False
            for key, value in ((k, v) for k, v in tasks_dict.items() if v[1] == "todo"):
                print(key, value[0], value[1], value[2], value[3])
                found = True
            
            if found == False:
                print("Nothing to display.")


def main():
    """Main function."""
    check_file(filename)
    parts = parse_input(users_input=input())

    match len(parts):
        case 1: 
            command = parts[0]
            id, description = None, None
        case 2:
            try:
                int(parts[1])
            except:
                command = parts[0]
                id = None
                description = parts[1]
            else:
                command = parts[0]
                id = parts[1]
                description = None
        case 3:
            command = parts[0]
            id = parts[1]
            description = parts[2]

    match command.lower():
        case "add":
            if description:
                add_task(description)
            elif id:
                crush_program("Incorrect arguments for \"add\" command.")
        case "delete":
            if id:
                delete_task(id)
            else:
                crush_program("Incorrect arguments for \"delete\" command.")
        case "update":
            if id and description:
                update_task(id, description)
            else:
                crush_program("Incorrect arguments for \"update\" command.")
        case "mark-in-progress":
            if id:
                status = "in-progress"
                update_status(id, status)
            else:
                crush_program("Incorrect arguments for \"mark-in-progress\" command.")
        case "mark-done":
            if id:
                status = "done"
                update_status(id, status)
            else:
                crush_program("Incorrect arguments for \"mark-done\" command.")
        case "list":
            if not description:
                show_full_list()
            elif description == "done":
                show_done_list()
            elif description == "in-progress":
                show_progress_list()
            elif description == "todo":
                show_todo_list()

if __name__ == "__main__":
    main()