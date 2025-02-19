class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi  

    def hitung_luas(self):
        return self.sisi ** 2  
    
    def hitung_keliling(self):
        return 4 * self.sisi  
    
#Objek kelas persegi
persegi1 = Persegi(4)  
persegi2 = Persegi(6)  


print(f"Luas persegi dengan sisi {persegi1.sisi}: {persegi1.hitung_luas()}")
print(f"Keliling persegi dengan sisi {persegi1.sisi}: {persegi1.hitung_keliling()}")

print(f"Luas persegi dengan sisi {persegi2.sisi}: {persegi2.hitung_luas()}")
print(f"Keliling persegi dengan sisi {persegi2.sisi}: {persegi2.hitung_keliling()}")
