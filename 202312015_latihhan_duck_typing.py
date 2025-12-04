class Laptop:
    def __init__(self, merk, ram):
        self.merk = merk
        self.ram = ram
    
    def nyalakan(self):
        return f"Laptop {self.merk} dengan RAM {self.ram}GB sedang booting..."

class Smartphone:
    def __init__(self, merk, sistem_operasi):
        self.merk = merk
        self.sistem_operasi = sistem_operasi
    
    def nyalakan(self):
        return f"Smartphone {self.merk} ({self.sistem_operasi}) menyala, logo muncul..."

def tes_nyala(obj):
    print(obj.nyalakan())

# Demonstrasikan duck typing dengan memanggil fungsi tersebut untuk kedua objek
# Membuat objek
laptop_asus = Laptop("ASUS", 16)
hp_iphone = Smartphone("iPhone", "iOS")

print("=== Demonstrasi Duck Typing ===")
print("\n1. Testing Laptop:")
tes_nyala(laptop_asus)

print("\n2. Testing Smartphone:")
tes_nyala(hp_iphone)

# Demonstrasi dengan list (polimorfisme)
print("\n=== Demonstrasi dengan List ===")
perangkat_list = [laptop_asus, hp_iphone]

for i, perangkat in enumerate(perangkat_list, 1):
    print(f"{i}. ", end="")
    tes_nyala(perangkat)

# Demonstrasi fungsi bekerja dengan objek lain yang memiliki method nyalakan()
print("\n=== Demonstrasi Ekstensi ===")

class Tablet:
    def __init__(self, merk, ukuran_layar):
        self.merk = merk
        self.ukuran_layar = ukuran_layar
    
    def nyalakan(self):
        return f"Tablet {self.merk} ({self.ukuran_layar}\") sedang menyala..."

tablet_samsung = Tablet("Samsung", 10.5)
print("Testing Tablet:")
tes_nyala(tablet_samsung)