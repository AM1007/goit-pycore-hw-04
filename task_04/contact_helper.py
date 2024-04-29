def add_contact(args: list, contacts: dict) -> str:
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except Exception as error:
        return f"add_contact error, {type(error)}, {error}"

def change_contact(args: list, contacts: dict) -> str:
    try:
        name, phone = args
        if not contacts.get(name):
            return "Contact does not exist"
        contacts[name] = phone
        return "Contact updated."
    except Exception as error:
        return f"change_contact error, {type(error)}, {error}"

def get_contact(args: list, contacts: dict) -> str:
    try:
        name = args[0]
        if not contacts.get(name):
            return "Contact does not exist"
        return f"{contacts.get(name)}"
    except Exception as error:
        return f"get_contact error, {type(error)}, {error}"

def get_all_contacts(contacts: dict) -> str:
    if not len(contacts):
        return "Contacts are empty"
    else:
        output = "Contacts:"
        for name, phone in contacts.items():
            output += f"\n{name}: {phone}"
        return output