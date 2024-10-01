class Kendaraan:
    def __init__(self, nama_instance, brand, model):
        self.nama_instance = nama_instance
        self.brand = brand
        self.model = model
    def bergerak(self):
        print("Bergerak!")

class Mobil(Kendaraan):
    def bergerak(self):
        print("Menyetir!")

class Kapal(Kendaraan):
    def bergerak(self):
        print("Berlayar!")

class Pesawat(Kendaraan):
    def bergerak(self):
        print("Terbang!")

mobil = Mobil("mobil", "McLaren", "Senna")
kapal = Kapal("kapal", "Ibiza", "Touring 20")
pesawat = Pesawat("pesawat", "Airbus", "a321")

# Menggunakan tuple
tuple_of_instance = (mobil, kapal, pesawat)
for kendaraan in tuple_of_instance:
    print(f"Nama Instance: {kendaraan.nama_instance}, Brand: {kendaraan.brand}, Model: {kendaraan.model}")
    kendaraan.bergerak()

# Menggunakan list
list_of_instance = [mobil, kapal, pesawat]
for kendaraan in list_of_instance:
    print(f"Nama Instance: {kendaraan.nama_instance}, Brand: {kendaraan.brand}, Model: {kendaraan.model}")
    kendaraan.bergerak()