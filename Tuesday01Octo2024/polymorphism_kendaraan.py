class Kendaraan:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Mobil(Kendaraan):
    def move(self):
        print("Drive!")

class Kapal(Kendaraan):
    def move(self):
        print("Sail!")

class Pesawat(Kendaraan):
    def move(self):
        print("Fly!")

mobil = Mobil("Toyota", "Corolla")
kapal = Kapal("Ibiza", "Touring 20")
pesawat = Pesawat("Boeing", "747")

for kendaraan in (mobil, kapal, pesawat):
    print(f"Brand: {kendaraan.brand}, Model: {kendaraan.model}")
    kendaraan.move()