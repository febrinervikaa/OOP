class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def tampilkan_info(self):
        print(f"Mobil {self.merek} berwarna {self.warna}")

mobil1 = Mobil("Rubicon", "Hitam")
mobil2 = Mobil("Civic", "HPutih")

mobil1.tampilkan_info()
mobil2.tampilkan_info()