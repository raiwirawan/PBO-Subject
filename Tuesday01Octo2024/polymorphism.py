# parent class yang bisa diextends
class Hewan:
    # fungsi yang harus ada, dan bisa dioverride oleh child class
    def suara(self):
        # passing fungsi suara agar langsung dapat digunakan pada child class
        pass

# child class Anjing meng-extends parent class Hewan
class Anjing(Hewan):
    # overriding fungsi suara pada parent class agar bersuara 'Bark'
    def suara(self):
        # mengembalikan string 'Bark'
        return 'Bark'

# child class Kucing meng-extends parent class Hewan
class Kucing(Hewan):
    # overriding fungsi suara pada parent class agar bersuara 'Meow'
    def suara(self):
        # mengembalikan string 'Meow'
        return 'Meow'
    
# child class Sapi meng-extends parent class Hewan
class Sapi(Hewan):
    # overriding fungsi suara pada parent class agar bersuara 'Moo'
    def suara(self):
        # mengembalikan string 'Moo'
        return 'Moo'
    
# fungsi bersuara yang berisi parameter hewan yang menerima argumen child classs
def bersuara(hewan):
    # meng-print parameter hewan yang seharusnya diisi oleh child class yg memiliki fungsi yang sama dengan parent class
    # parameter hewan yang berisi class hewan lalu dipanggilkan fungsi suara
    print(hewan.suara())

bersuara(Sapi())
bersuara(Anjing())
bersuara(Kucing())