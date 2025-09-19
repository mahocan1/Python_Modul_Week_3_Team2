# Ana sınıf (Şekil)
class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik


# Dikdörtgen sınıfı
class Dikdortgen(Sekil):
    def calculate_area(self):
        return self.genislik * self.yukseklik


# Kare sınıfı
class Kare(Sekil):
    def calculate_area(self):
        return self.genislik * self.yukseklik


# Örnek kullanımlar:
dikdortgen = Dikdortgen(5, 10)   # genişlik=5, yükseklik=10
kare = Kare(7, 7)               # genişlik=7, yükseklik=7

print(f"Dikdörtgenin Alanı: {dikdortgen.calculate_area()}")
print(f"Karenin Alanı: {kare.calculate_area()}")
