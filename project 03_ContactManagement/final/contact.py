class Contact:

    def __init__(self, contact_id, name, phone_number, email):

        self.id = contact_id
        self.name = name
        self.phone_number = phone_number
        self.email = email


    def show_info(self):

        print(f"""
        Contact ID : {self.id}
        Name : {self.name}
        Phone Number : {self.phone_number}
        Email : {self.email}
        """)


    def update(self, name, phone_number, email):

        self.name = name
        self.phone_number = phone_number
        self.email = email



    def to_dict(self):

        return{
            "ID" : self.id,
            "Name" : self.name,
            "Phone Number" : self.phone_number,
            "Email" : self.email
        }