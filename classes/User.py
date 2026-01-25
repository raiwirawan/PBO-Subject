class User:
    def __init__(self, user_id, username, age, address):
        self.__user_id = user_id
        self.__username = username
        self.__age = age
        self.__address = address

    def set_user_id(self, new_user_id):
        self.__user_id = new_user_id

    def get_user_id(self):
        return self.__user_id
    
    def set_username(self, new_username):
        self.__username = new_username

    def get_username(self):
        return self.__username
    
    def set_age(self, new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age
    
    def set_address(self, new_address):
        self.__address = new_address

    def get_address(self):
        return self.__address
    
