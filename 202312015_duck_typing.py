class Burning:
    def terbang(self):
        return "Burning terbang tinggi"

class Pesswat:
    def terbang(self):
        return "Pesswat lepas landas"

def uji_terbang(obj):
    print(obj.terbang())

# Duck typing dalam aksi
b = Burning()
p = Pesswat()

uji_terbang(b)
uji_terbang(p)