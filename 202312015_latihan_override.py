class Bentuk:
    def luas(self):
        return 0

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def luas(self):
        import math
        return math.pi * self.jari_jari * self.jari_jari

# Demonstrasikan pemanggilan method luas() dari objek masing-masing class
# Membuat objek
bentuk_umum = Bentuk()
persegi = Persegi(5)
lingkaran = Lingkaran(7)

# Demonstrasi polimorfisme
daftar_bentuk = [bentuk_umum, persegi, lingkaran]

print("=== Hasil Perhitungan Luas ===")
for i, bentuk in enumerate(daftar_bentuk, 1):
    if isinstance(bentuk, Bentuk):
        nama = "Bentuk Umum"
    elif isinstance(bentuk, Persegi):
        nama = f"Persegi (sisi = {bentuk.sisi})"
    elif isinstance(bentuk, Lingkaran):
        nama = f"Lingkaran (jari-jari = {bentuk.jari_jari})"
    
    print(f"{i}. {nama}: {bentuk.luas():.2f}")

print("\n=== Pemanggilan Langsung ===")
print(f"Bentuk umum: {bentuk_umum.luas()}")
print(f"Persegi (sisi 5): {persegi.luas()}")
print(f"Lingkaran (jari-jari 7): {lingkaran.luas():.2f}")