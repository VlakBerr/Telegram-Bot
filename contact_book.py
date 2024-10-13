class UserContact:
    def __init__(self,
                 name:str,
                 phone_number:str,
                 discription:str = "" ):
        self.name = name 
        self.phone_number = phone_number
        self.discription = discription

    def __str__(self):
        return f'Имя: {self.name}, Номер телефона: {self.phone_number}'


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,
                 name:str,
                 phone_number:str,
                 discription:str = "" ):
        contact = UserContact(name, phone_number, discription)
        self.contacts.append(contact)

    def find_contact(self, name):
        found_contacts = []

        for contact in self.contacts:
            if contact.name == name:
                found_contacts.append(contact)
        return self.contacts
    
    def get_contacts(self):
        return self.contacts
    

class ContactBuilder:
    def add_name(self, name):
        pass

    def add_phone_number(self, phone_number):
        pass

    def add_discription(self, discriprion):
        pass
    
