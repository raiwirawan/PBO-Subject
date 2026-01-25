# Class Animal (Superclass)
#made by gulem 
class Animal:
    def __init__(self, name, umur):
        self.name = name
        self.umur = umur

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def live_long(self):
        print(f"{self.name} is living until {self.umur} age.")


# Class Mammal (Subclass)
class Mammal(Animal):
    def __init__(self, name, umur, fur_color):
        super().__init__(name, umur)  # Membuat objek Animal terlebih dahulu
        self.fur_color = fur_color

    def nurse(self):
        print(f"{self.name} is nursing its young.")

    def groom(self):
        print(f"{self.name} is grooming itself with {self.fur_color} fur.")
    
class Reptile(Animal):
    def __init__(self, name, umur, pattern_color):
        super().__init__(name, umur)
        self.pattern_color = pattern_color

    def pattern(self):
        print(f"{self.name} has {self.pattern_color} pattern")
    
    def live_long(self):
        print(f"{self.name} is living until {self.umur} age")

class Human(Mammal):
    def __init__(self, name, umur, fur_color, legs, avg_walk_speed, avg_run_speed):
        super().__init__(name, umur, fur_color)
        self.legs = legs
        self.avg_walk_speed = avg_walk_speed
        self.avg_run_speed = avg_run_speed
    
    def walk(self):
        print(f"{self.name} can walk with {self.legs} legs on {self.avg_walk_speed}Km/h speed")
    
    def run(self):
        print(f"{self.name} can run with {self.legs} legs on {self.avg_run_speed}Km/h speed")


# Contoh penggunaan
if __name__ == "__main__":
    mammal = Mammal("Cat", 8, "Black")

    mammal.eat()
    mammal.sleep()
    mammal.nurse()
    mammal.groom()
    mammal.live_long()
    
    reptile = Reptile('Snake', 12, 'Yellow Black')

    reptile.eat()
    reptile.sleep()
    reptile.live_long()
    reptile.pattern()


    human = Human('Rai Wirawan', 19, 'Brow', 2, 10, 30)

    human.eat()
    human.sleep()
    human.live_long()
    human.walk()
    human.run()