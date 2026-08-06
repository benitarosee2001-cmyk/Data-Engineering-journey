import json

contacts = []

def show_menu():

    print("===== Contacts =====")
    print("1.Add Contact")
    print("2.Show Contacts")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Save")
    print("6.Load")
    print("7.Exit")
    print("-" * 50)


def add_contact():

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "Name" : name,
        "Phone" : phone,
        "Email" : email
    }

    contacts.append(contact)
    print("Contact Added Successfully.")


def show_contact():

    if len(contacts) == 0:
        print("No contact found.")
    else:
        print("===== Contacts =====")

        for contact in contacts:
            print(f"Name: {contact['Name']}")
            print(f"phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print("*" * 50)


def search_contact():

    name = input("Name: ")

    found = False

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            print(f"Name: {contact['Name']}")
            print(f"phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            found = True
            break
    
    if not found:
        print("Contact not found.")

def delete_contact():

    name = input("Name: ")

    found = False

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.")
            found = True
            break

    if not found:
        print("Contact not found.")


def save_contact():

    with open("Contacts.json", "w", encoding="utf8") as file:
        json.dump(contacts, file, indent=4)

    
    print("Contact save successfully.")


def load_contact():

    global contacts

    with open("Contacts.json", "r", encoding="utf8") as file:
        contacts = json.load(file)

    
    print("Contact load successfully.")


def main():

    while True:

        show_menu()

        choice = input("Choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contact()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            save_contact()

        elif choice == "6":
            load_contact()

        elif choice == "7":
            print("Good Bye!")
            break

        else:
            print("Invalid choice.")

main()