def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args
def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid input. Use: add [name] [phone]"
def chenge_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid input. Use: change [name] [phone]"
def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"{name}: {contacts[name]}"
        else:
            return "Contact not found."
    except IndexError:
        return "Invalid input. Use: show [name]"
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        if command in ("close", "exit"):
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()                                        
