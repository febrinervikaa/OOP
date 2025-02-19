class Manusia:
    def __init__(self, Nama, Umur):
        self.Nama = Nama
        self.Umur = Umur

    def tampilkan_data(self):
        print("Nama  : " + self.Nama)
        print("Umur  : " + str(self.Umur))  

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))

Manusia = Manusia(nama, umur)
Manusia.tampilkan_data()