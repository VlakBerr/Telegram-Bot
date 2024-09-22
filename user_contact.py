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
    
