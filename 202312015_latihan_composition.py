class Penulis:
    def __init__(self, nama, asal_negara=""):
        self.nama = nama
        self.asal_negara = asal_negara
    
    def info_penulis(self):
        if self.asal_negara:
            return f"Penulis: {self.nama} ({self.asal_negara})"
        return f"Penulis: {self.nama}"

class Buku:
    def __init__(self, judul, penulis, tahun_terbit, genre=""):
        self.judul = judul
        self.penulis = penulis  # Composition - Buku memiliki objek Penulis
        self.tahun_terbit = tahun_terbit
        self.genre = genre
    
    def info_buku(self):
        info = f"Buku: {self.judul}\n"
        info += f"  - {self.penulis.info_penulis()}\n"
        info += f"  - Tahun Terbit: {self.tahun_terbit}"
        
        if self.genre:
            info += f"\n  - Genre: {self.genre}"
        
        return info
    
    def ubah_penulis(self, penulis_baru):
        """Metode untuk mengubah penulis buku"""
        self.penulis = penulis_baru
        return f"Penulis buku '{self.judul}' telah diubah menjadi {penulis_baru.nama}"

# Demonstrasi cara mengakses data penulis dari objek buku
# Membuat objek Penulis
penulis1 = Penulis("Andrea Hirata", "Indonesia")
penulis2 = Penulis("Tere Liye")
penulis3 = Penulis("J.K. Rowling", "Inggris")

# Membuat objek Buku dengan composition
buku1 = Buku("Laskar Pelangi", penulis1, 2005, "Novel")
buku2 = Buku("Bumi", penulis2, 2014, "Fantasi")
buku3 = Buku("Harry Potter and the Philosopher's Stone", penulis3, 1997, "Fantasi")

print("=== INFORMASI BUKU DAN PENULIS ===")
print("=" * 40)

# Menampilkan informasi buku lengkap
print("1. Informasi Buku Lengkap:")
print(buku1.info_buku())
print()

print("2. Informasi Buku Lengkap:")
print(buku3.info_buku())
print()

# Demonstrasi mengakses data penulis dari objek buku
print("3. Mengakses Data Penulis dari Objek Buku:")
print(f"Judul buku: {buku2.judul}")
print(f"Nama penulis: {buku2.penulis.nama}")
print(f"Asal negara penulis: {buku2.penulis.asal_negara if buku2.penulis.asal_negara else 'Tidak diketahui'}")
print()

# Demonstrasi perubahan penulis
print("4. Demonstrasi Mengubah Penulis:")
print(f"Sebelum: {buku2.penulis.nama}")
print(buku2.ubah_penulis(Penulis("Dee Lestari", "Indonesia")))
print(f"Sesudah: {buku2.penulis.nama}")
print()

# Menampilkan semua buku dengan penulisnya
print("5. Daftar Semua Buku dan Penulis:")
daftar_buku = [buku1, buku2, buku3]

for i, buku in enumerate(daftar_buku, 1):
    print(f"{i}. {buku.judul} - {buku.penulis.nama} ({buku.tahun_terbit})")

# Demonstrasi hubungan composition yang kuat
print("\n6. Demonstrasi Hubungan Composition:")
print("Objek Penulis dapat hidup sendiri:")
print(f"Penulis: {penulis1.nama} - {'dari ' + penulis1.asal_negara if penulis1.asal_negara else ''}")

print("\nTapi objek Buku membutuhkan objek Penulis:")
try:
    # Ini akan menyebabkan error karena buku membutuhkan objek Penulis
    buku_tanpa_penulis = Buku("Buku Tanpa Penulis", None, 2023)
    print(buku_tanpa_penulis.info_buku())
except AttributeError as e:
    print(f"Error: Tidak bisa membuat buku tanpa penulis - {e}")