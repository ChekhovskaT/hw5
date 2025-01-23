def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and phone, please."
        except KeyError:
            return "This contact doesn't exist."
        except IndexError:
            return "Invalid input. Please provide the correct arguments."
    return inner

@input_error
def add_contacts(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact added."

@input_error
def change_contact(args, contacts):
    # Сheck if arguments contain two elements
    if len(args) != 2:
        raise ValueError("Invalid arguments. Usage: change [name] [new_phone]")
    # Unpack arguments
    name, new_phone = args
    # Check if the contact exists in the dictionary
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact changed: {name} -> {new_phone}"
    else:
        raise KeyError(f"Contact '{name}' not found.") 


@input_error
def show_phone(args, contacts):
    # Check if one argument (name) is provided
    if len(args) != 1:
        raise ValueError("Invalid arguments. Usage phone [name]")
    # Extract the contact's name
    name = args[0]
    # Check if the contact exists in the dictionary
    if name in contacts:
        return f"Contact {name}: {contacts[name]}"
    else:
        raise KeyError(f"Contact '{name}' not found.")

@input_error
def show_all(contacts):
    # Checking for dictionary emptiness:
    if not contacts: 
        return "No contacts found."
    #Create a list to save results
    result = ["Contacts list:"]
    # Add names and phone numbers from the dictionary to the list
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    # Concatenate a list into a multi-line string
    return "\n".join(result) 


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contacts(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()