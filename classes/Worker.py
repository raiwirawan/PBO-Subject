from User import User

class Worker(User):
    def __init__(self, user_id, username, age, address):
        super().__init__(user_id, username, age, address)

    def work(self):
        print(self.get_username(), " is still working")