class RandomCharsGenerator:
    def __init__(self, length):
        self.__length = length
        self.__lowercase_alphabets = 'abcdefghijklmnopqrstuvwxyz'
        self.__uppercase_alphabets = self.__lowercase_alphabets.capitalize()
        self.__numerics = '0123456789'
        self.__chars = self.__lowercase_alphabets + self.__uppercase_alphabets + self.__numerics
        self.__list_of_chars = list(self.__chars)

    def generate(self):
        result =''
        for i in self.__list_of_chars:
            result += i
        return result
    

generator = RandomCharsGenerator(9)