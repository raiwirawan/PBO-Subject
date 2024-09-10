class MyMethods:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adding_nums(self):
        print(self.x + self.y)
    
    def subtract_nums(self):
        print(self.x - self.y)
    
    def multiply_nums(self):
        print(self.x * self.y)
    
    def divide_nums(self):
        print(self.x / self.y)

methods = MyMethods(8, 5)

methods.adding_nums()
methods.subtract_nums()
methods.multiply_nums()
methods.divide_nums()