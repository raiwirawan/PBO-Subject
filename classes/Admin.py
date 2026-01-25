from User import User

class Admin(User):
    def __init__(self, user_id, username, age, address):
        super().__init__(user_id, username, age, address)

    def create(self):
        print('create something')

    def read(self):
        print('read something')

    def update(self):
        print('update something')
        
    def delete(self):
        print('delete something')