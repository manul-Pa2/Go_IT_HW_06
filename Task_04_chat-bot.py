def parse_input(user_input: str):
    user_input = user_input.strip()
    if not user_input:
        return "", []    # щоб main() не ловив винятки на порожньому рядку

    parts = user_input.split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def _validate_phone(phone: str) -> bool:     # не обов'язково, але корисно
    return phone.isdigit() and len(phone) == 10


def add_contact(args, contacts: dict) -> str:    
    if len(args) < 2:
        return "Invalid command. Use: add <name> <phone>"

    name, phone = args[0], args[1]

    if not _validate_phone(phone):
        return "Phone number must contain exactly 10 digits."

    message = "Contact updated." if name in contacts else "Contact added."
    contacts[name] = phone
    return message


def change_contact(args, contacts: dict) -> str:
    if len(args) < 2:
        return "Invalid command. Use: change <name> <phone>"

    name, phone = args[0], args[1]

    if name not in contacts:
        return "Contact not found."

    if not _validate_phone(phone):
        return "Phone number must contain exactly 10 digits."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts: dict) -> str:
    if len(args) < 1:
        return "Invalid command. Use: phone <name>"

    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts found."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
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
