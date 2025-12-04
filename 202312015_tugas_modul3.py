# Class Parent: Karyawan
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
    
    def info_gaji(self):
        return f"{self.nama}: Gaji Pokok = Rp {self.gaji_pokok:,.2f}"

# Child Class: Manager (inherits Karyawan)
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan
    
    def info_gaji(self):
        gaji_total = self.gaji_pokok + self.tunjangan
        return f"{self.nama}: Gaji Pokok = Rp {self.gaji_pokok:,.2f}, Tunjangan = Rp {self.tunjangan:,.2f}, Total = Rp {gaji_total:,.2f}"

# Child Class: Programmer (inherits Karyawan)
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus
    
    def info_gaji(self):
        gaji_total = self.gaji_pokok + self.bonus
        return f"{self.nama}: Gaji Pokok = Rp {self.gaji_pokok:,.2f}, Bonus = Rp {self.bonus:,.2f}, Total = Rp {gaji_total:,.2f}"

# Composition: Class Departemen
class Departemen:
    def __init__(self, nama_departemen):
        self.nama_departemen = nama_departemen
        self.daftar_karyawan = []  # Composition: memiliki daftar objek karyawan
    
    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)
        return f"{karyawan.nama} berhasil ditambahkan ke departemen {self.nama_departemen}"
    
    def tampilkan_karyawan(self):
        if not self.daftar_karyawan:
            print(f"Tidak ada karyawan di departemen {self.nama_departemen}")
            return
        
        print(f"\n{'='*60}")
        print(f"DAFTAR KARYAWAN - DEPARTEMEN {self.nama_departemen.upper()}")
        print(f"{'='*60}")
        
        total_gaji_departemen = 0
        for i, karyawan in enumerate(self.daftar_karyawan, 1):
            # Polymorphism: memanggil info_gaji() yang berbeda untuk tiap jenis karyawan
            print(f"{i}. {karyawan.info_gaji()}")
            
            # Hitung total gaji berdasarkan jenis karyawan
            if isinstance(karyawan, Manager):
                total_gaji_departemen += karyawan.gaji_pokok + karyawan.tunjangan
            elif isinstance(karyawan, Programmer):
                total_gaji_departemen += karyawan.gaji_pokok + karyawan.bonus
        
        print(f"{'='*60}")
        print(f"Total Gaji Departemen: Rp {total_gaji_departemen:,.2f}")
        print(f"Jumlah Karyawan: {len(self.daftar_karyawan)}")
        
        # Statistik karyawan
        jumlah_manager = sum(1 for k in self.daftar_karyawan if isinstance(k, Manager))
        jumlah_programmer = sum(1 for k in self.daftar_karyawan if isinstance(k, Programmer))
        print(f"Rincian: {jumlah_manager} Manager, {jumlah_programmer} Programmer")
    
    def cari_karyawan(self, nama):
        for karyawan in self.daftar_karyawan:
            if karyawan.nama.lower() == nama.lower():
                return karyawan
        return None
    
    def total_pengeluaran_gaji(self):
        total = 0
        for karyawan in self.daftar_karyawan:
            if isinstance(karyawan, Manager):
                total += karyawan.gaji_pokok + karyawan.tunjangan
            elif isinstance(karyawan, Programmer):
                total += karyawan.gaji_pokok + karyawan.bonus
        return total

# Instansiasi dan Demonstrasi
def main():
    print("=== SISTEM MANAJEMEN KARYAWAN ===\n")
    
    # Buat 2 Manager dan 2 Programmer
    print("1. Membuat Objek Karyawan:")
    print("-" * 40)
    
    manager1 = Manager("Budi Santoso", 15000000, 5000000)
    manager2 = Manager("Siti Nurhaliza", 18000000, 7000000)
    programmer1 = Programmer("Andi Wijaya", 12000000, 3000000)
    programmer2 = Programmer("Rina Melati", 13000000, 3500000)
    
    print(f"✓ {manager1.nama} (Manager) dibuat")
    print(f"✓ {manager2.nama} (Manager) dibuat")
    print(f"✓ {programmer1.nama} (Programmer) dibuat")
    print(f"✓ {programmer2.nama} (Programmer) dibuat")
    
    # Tambahkan ke dalam departemen
    print("\n2. Membuat Departemen dan Menambahkan Karyawan:")
    print("-" * 40)
    
    dept_it = Departemen("Teknologi Informasi")
    
    print(dept_it.tambah_karyawan(manager1))
    print(dept_it.tambah_karyawan(manager2))
    print(dept_it.tambah_karyawan(programmer1))
    print(dept_it.tambah_karyawan(programmer2))
    
    # Tambahkan beberapa karyawan lagi untuk variasi
    programmer3 = Programmer("Joko Susilo", 11000000, 2500000)
    print(dept_it.tambah_karyawan(programmer3))
    
    # Tampilkan info gaji semua karyawan
    print("\n3. Informasi Gaji Karyawan:")
    print("-" * 40)
    
    # Demonstrasi polymorphism pada level individu
    print("\nInfo Gaji Per Individu:")
    print(f"a. {manager1.info_gaji()}")
    print(f"b. {programmer1.info_gaji()}")
    
    # Tampilkan semua karyawan di departemen
    dept_it.tampilkan_karyawan()
    
    # Demonstrasi fitur tambahan
    print("\n4. Fitur Tambahan:")
    print("-" * 40)
    
    # Mencari karyawan
    nama_cari = "Budi Santoso"
    karyawan_ditemukan = dept_it.cari_karyawan(nama_cari)
    if karyawan_ditemukan:
        print(f"✓ Karyawan ditemukan: {karyawan_ditemukan.info_gaji()}")
    else:
        print(f"✗ Karyawan '{nama_cari}' tidak ditemukan")
    
    # Total pengeluaran gaji
    total_gaji = dept_it.total_pengeluaran_gaji()
    print(f"✓ Total pengeluaran gaji departemen: Rp {total_gaji:,.2f}")
    
    # Demonstrasi inheritance dan polymorphism dengan list
    print("\n5. Demonstrasi Inheritance & Polymorphism:")
    print("-" * 40)
    
    semua_karyawan = [manager1, manager2, programmer1, programmer2, programmer3]
    
    print("Menggunakan loop dengan polymorphism:")
    for karyawan in semua_karyawan:
        # Polimorfisme: method info_gaji() akan dipanggil sesuai class asalnya
        print(f"  - {karyawan.info_gaji()}")
    
    print("\n=== PROGRAM SELESAI ===")

if __name__ == "__main__":
    main()