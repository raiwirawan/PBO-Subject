class Hero:
    def __init__(self, gender, nama, umur, range):
        self.gender = gender
        self.nama = nama
        self.umur = umur
        self.range = range

class Assasin(Hero):
    pass
    def __init__(self, gender, nama, umur, range, pedang):
        super().__init__(gender, nama, umur, range)
        self.pedang = pedang
    
    def membunuh(self):
        print(f"{self.nama} which is Assassin is using {self.pedang} that have {self.range} Km")


class Marksman(Hero):
    pass
    def __init__(self, gender, nama, umur, range, pistol):
        super().__init__(gender, nama, umur, range)
        self.pistol = pistol

    def menembak(self):
        print(f"{self.nama} which is Marksman is using {self.pistol} that have {self.range} Km")

class Fighter(Hero):
    pass
    def __init__(self, gender, nama, umur, range, melee):
        super().__init__(gender, nama, umur, range)
        self.melee = melee
    
    def __str__(self):
        return f"{self.nama} which is Fighter is using {self.melee} that have {self.range} Km\nDone bang!"


roger = Marksman("Man", "Roger Sumatra", 25, 12, "Kar 98")
roger.menembak()

ling = Assasin("Man", "Ling lawak", 18, 1, "Penghancur Dunia")
ling.membunuh()

yu = Fighter("Man", "Yu", 18, 0.2, "Fist")
print(yu)