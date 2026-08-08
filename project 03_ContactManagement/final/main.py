from contact import Contact
from database import load_contacts, save_contacts
from utils import generate_id, update_last_id

contacts = load_contacts()
update_last_id(contacts)


def show_menu():

    print("""
========== Contact Management ==========
1. Add Contact
2. Show Contacts
3. Search Contact by ID
4. Edit Contact
5. Delete Contact
6. Count Contacts
7. Save Contacts
8. Load Contacts
9. Statistics
10. Exit
========================================
""")


def add_contact():

    name = input("Name: ")
    email = input("Email: ")

    for contact in contacts:
        if contact.name.lower() == name.lower() and contact.email.lower() == email.lower():
            print("Contact already exists.")
            return

    try:

        phone = int(input("Phone: "))

        if phone <= 0:
            print("Invalid Phone Number.")
            return

    except ValueError:
        print("Invalid input.")
        return

    contact_id = generate_id()

    new_contact = Contact(
        contact_id,
        name,
        phone,
        email
    )

    contacts.append(new_contact)

    print(f"Contact added successfully. ID = {new_contact.id}")


def show_contact():

    if not contacts:
        print("No contact found.")
        return

    for contact in contacts:
        contact.show_info()


def search_contact():

    try:

        search_id = int(input("Contact ID: "))

    except ValueError:
        print("Invalid ID.")
        return

    for contact in contacts:
        if contact.id == search_id:
            contact.show_info()
            return

    print("Contact not found.")


def edit_contact():

    try:

        edit_id = int(input("Contact ID: "))

    except ValueError:
        print("Invalid ID.")
        return

    for contact in contacts:
        if contact.id == edit_id:

            name = input("Name: ")
            email = input("Email: ")

            try:

                phone = int(input("Phone: "))

                if phone <= 0:
                    print("Invalid Phone Number.")
                    return

            except ValueError:
                print("Invalid Input.")
                return

            contact.update(
                name,
                phone,
                email
                )

            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact():

    try:

        delete_id = int(input("Contact ID: "))

    except ValueError:
        print("Invalid ID.")
        return


    for contact in contacts:
        if contact.id == delete_id:
            contacts.remove(contact)
            print("Contact removed successfully.")
            return

    print("Contact not found.")


def count_contact():

    print(f"Total Contacts: {len(contacts)}")


def statistics():

    if not contacts:
        print("No contacts found.")
        return

    print("\n======== Statistics ========")
    print(f"Total Contacts: {len(contacts)}")


def main():

    global contacts

    while True:

        show_menu()

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        
        elif choice == "2":
            show_contact()
        
        elif choice == "3":
            search_contact()
        
        elif choice == "4":
            edit_contact()
        
        elif choice == "5":
            delete_contact()
        
        elif choice == "6":
            count_contact()
        
        elif choice == "7":
            save_contacts(contacts)
        
        elif choice == "8":
            contacts = load_contacts()
            update_last_id(contacts)
        
        elif choice == "9":
            statistics()
        
        elif choice == "10":
            print("Good Bye.")
            break
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()