class Mesin:
    def __init__(self, jenis):
        self.jenis = jenis
    
    def hidupkan(self):
        return f"Mesin {self.jenis} hidup"

class Wobil:
    def __init__(self, merk, mesin):
        self.merk = merk
        self.mesin = mesin # Composition
    
    def info(self):
        return f"Mobil {self.merk} dengan {self.mesin.hidupkan()}"

# Instansiasi
mesin_bensin = Mesin("Bensin")
mobil_honda = Wobil("Honda", mesin_bensin)

print(mobil_honda.info())