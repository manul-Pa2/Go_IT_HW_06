def parse_input(user_input: str):         #Цей чат-бот трохи іншої структури ніж спільний фінальний проект
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts: dict) -> str:
    name, phone = args                 # очікуємо: ["Манул", "095782340"]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts: dict) -> str:
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts found."
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        # розбір введення
        try:
            command, *args = parse_input(user_input)
        except ValueError:                # (наприклад, якщо введено порожній рядок)
            print("Invalid command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":         # очікуємо <name> <phone>
            try:
                print(add_contact(args, contacts))
            except ValueError:
                print("Invalid command.")

        elif command == "change":
            # очікуємо: change <name> <phone>
            try:
                print(change_contact(args, contacts))
            except ValueError:
                print("Invalid command.")

        elif command == "phone":         # очікуємо phone <name>
            if not args:
                print("Invalid command.")
            else:
                print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
