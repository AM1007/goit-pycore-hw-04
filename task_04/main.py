from contact_helper import add_contact, change_contact, get_contact, get_all_contacts

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "all":
                    print(get_all_contacts(contacts))
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(get_contact(args, contacts))
                case _:
                    print("Invalid command.")

if __name__ == "__main__":
    main()