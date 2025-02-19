class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"Produk {self.nama} {self.harga}"

Produk1 = Produk("Basreng", "10.000")
Produk2 = Produk("Kripca", "12.000")

# Mengakses metode dari objek
print(Produk1.info())  
print(Produk2.info())  