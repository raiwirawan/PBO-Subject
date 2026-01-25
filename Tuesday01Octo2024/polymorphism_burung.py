class Burung:
    def intro(self):
        print("Di dunia ini ada beberapa type berbeda dari spesies burung")
    def terbang(self):
        print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak dapat terbang")

class Elang(Burung):
    def terbang(self):
        print("Elang dapat terbang")

class BurungUnta(Burung):
    def terbang(self):
        print("Burung unta tidak dapat terbang")

def cetak_info_burung(burung):
    burung.intro()
    burung.terbang()

obj_burung = Burung()
obj_elang = Elang()
obj_burung_unta = BurungUnta()

cetak_info_burung(obj_burung)
cetak_info_burung(obj_elang)
cetak_info_burung(obj_burung_unta)