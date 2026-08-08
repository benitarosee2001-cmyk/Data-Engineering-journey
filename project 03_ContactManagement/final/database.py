import json

from contact import Contact

FILE_NAME = "Contacts.json"


def save_contacts(contacts):

    data = []

    for contact in contacts:
        data.append(contact.to_dict())

    with open(FILE_NAME, "w", encoding="utf8") as file:
        json.dump(data, file, indent=4)

    print("Contact saved successfully.")


def load_contacts():

    contacts = []

    try:

        with open(FILE_NAME, "r", encoding = "utf8") as file:
            data = json.load(file)

            for item in data:

                contact = Contact(
                    item["ID"],
                    item["Name"],
                    item["Phone Number"],
                    item["Email"]
                )

                contacts.append(contact)

            print("Contact loaded successfully.")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("Invalid json data")

    return contacts