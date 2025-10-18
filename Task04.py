def parse_input(user_input: str):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


def add_contact(args, contacts: dict) -> str:
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts: dict) -> str:
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts: dict) -> str:
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts saved."
    # один рядок на контакт
    return "\n".join(f"{n}: {p}" for n, p in contacts.items())


def main():
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print("Invalid command.")
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
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
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
