# parent class Hewan yang berisi fungsi bicara()
class Hewan:
    def bicara(self):
        print("Hewan berbicara")

# child class Kucing yang meng-extend parent class Hewan yang berisi fungsi bicara()
class Kucing(Hewan):
    def meaow(self):
        print("meaow....meaow....meaow..!!!")

# grandchild class AnakKucing yang meng-extend child class Kucing yang berisi fungsi bicara()
class AnakKucing(Kucing):
    def minum(self):
        print("minum susu")

# fungsi cetak_suara yang menerima argumen class
def cetak_suara(hewan):
    hewan.bicara()
    if hasattr(hewan, 'meaow'):
        hewan.meaow()
    if hasattr(hewan, 'minum'):
        hewan.minum()

a_k = AnakKucing()
cetak_suara(a_k)