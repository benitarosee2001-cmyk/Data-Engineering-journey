contact_id = 1000


def generate_id():

    global contact_id

    contact_id += 1

    return contact_id


def update_last_id(contacts):

    global contact_id

    if not contacts:
        contact_id = 1000
        return

    contact_id = max(contact.id for contact in contacts)