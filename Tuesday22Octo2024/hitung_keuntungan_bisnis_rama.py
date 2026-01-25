class Dividen:
    def __init__(self, lembar_saham_dimiliki, laba_kotor):
        self.seratus_persen = 1
        self.total_saham = 30
        self.lembar_saham_dimiliki = lembar_saham_dimiliki
        self.laba_kotor = laba_kotor
        self.dividen = 0
    
    def hitung_dividen(self):
        self.dividen = (self.seratus_persen / self.total_saham) * self.lembar_saham_dimiliki * self.laba_kotor
        return self.dividen
    
    def dividen_perbulan(self):
        return self.dividen / 12

scenarios = [
    {
        "lembar_saham_dimiliki": 1,
        "laba_kotor": 200000000
    },
    {
        "lembar_saham_dimiliki": 1,
        "laba_kotor": 1000000000
    },
    {
        "lembar_saham_dimiliki": 2,
        "laba_kotor": 200000000
    },
    {
        "lembar_saham_dimiliki": 2,
        "laba_kotor": 1000000000
    },
]

i = 1
for scenario in scenarios:
    dividen = Dividen(scenario.get("lembar_saham_dimiliki"), scenario.get("laba_kotor"))
    print(f"\nSkenario {i}")
    print("\n--- Keterangan ---")
    print(f"Lembaran saham dimiliki : {scenario.get("lembar_saham_dimiliki")}")
    print(f"Laba kotor : {scenario.get("laba_kotor")}")
    print("\n--- Pendapatan ---")
    print(f"Pertahun {round(dividen.hitung_dividen(), 0)}")
    print(f"Perbulan: {round(dividen.dividen_perbulan(), 0)}")
    print("\n============================")
    i+=1