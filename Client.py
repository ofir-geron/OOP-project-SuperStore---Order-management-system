import re

class Client :
    def __init__(self, client_id, name, email, address, phone_number, gender):
        if isinstance(client_id, int) == True:
            self.client_id = client_id
        else:
            self.client_id = 11111  # if client id will be 11111111 we will know that the original id wasn't valid
        self.name = name
        if Client.check_mail(email):
            self.email = email
        else:
            self.email= 'NotValid@gmail.com' #if mail not valid, the mail will be 'NotValid@gmail.com'
        self.address = address
        self.phone_number = phone_number
        if gender=='M' or gender=='F':
            self.gender = gender
        else:
            self.gender= 'F' #if gender not valid, the gender will be F

    @staticmethod
    def check_mail(email: str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.search(regex, email):
            return True
        else:
            return False

    def print_me(self):
        print("client id: ", self.client_id)
        print("name: ", self.name)
        print("email: ", self.email)
        print("address: ", self.address)
        print("phone_number: ", self.phone_number)
        print("gender: ", self.gender)

    def __str__(self):
        return f"{self.client_id},{self.name},{self.email},{self.address},{self.phone_number},{self.gender}"

    def __repr__(self):
        return str(self)

