import json
filename = "users_task.json"


def check_file(filename):
    """The function checks if a file exists in a directory and creates it otherwise."""
    try:
        with open(filename, 'x'):
            pass
    except FileExistsError:
        pass


def crush_program(reason):
    """Function terminates the program when an error occurs."""
    raise SystemExit(f"Error: {reason}")
    

def parse_input(users_input):
    """Function splits a string into parts, taking into account spaces and quotation marks."""
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
    """Function adds a new task to our dictionary."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            id = 1
            tasks_dict[id] = data
        else:
            id = len(tasks_dict) + 1
            tasks_dict[id] = data

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)


def delete_task(id):
    """Function delete a task to our dictionary."""
    pass


def update_task(id, data):
    """Function update a current task to our dictionary."""
    tasks_dict = {}
    with open(filename, 'r') as file:
        try:
            tasks_dict = json.load(file)
        except:
            crush_program("You can't update the task because the to-do list is empty now.")
        else:
            if id in tasks_dict.keys():
                key_exists = True
            else:
                key_exists = False
            
            if key_exists:
                tasks_dict[id] = data
            else:
                crush_program("You can't update this task because it's not on the to-do list.")

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)


def main():
    """Main function."""
    check_file(filename)
    parts = parse_input(users_input=input())

    match len(parts):
        case 1: 
            command = parts[0]
            id, description = None
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

    match command:
        case "add":
            if description:
                add_task(description)
            elif id:
                crush_program("Incorrect arguments for \"add\" command.")
        case "delete":
            pass
        case "update":
            if id and description:
                update_task(id, description)
            else:
                crush_program("Incorrect arguments for \"update\" command.")

if __name__ == "__main__":
    main()