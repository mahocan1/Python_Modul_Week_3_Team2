# Temel sınıf
class Vehicle:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def display_info(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}")


# Arazi Aracı (SUV) sınıfı
class SUV(Vehicle):
    def __init__(self, marka, model, yil, dort_ceker):
        super().__init__(marka, model, yil)
        self.dort_ceker = dort_ceker  # True/False

    def display_info(self):
        super().display_info()
        print(f"Dört Tekerlekten Çekiş: {'Evet' if self.dort_ceker else 'Hayır'}")


# Spor Araba sınıfı
class SportCar(Vehicle):
    def __init__(self, marka, model, yil, max_speed):
        super().__init__(marka, model, yil)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Maksimum Hız: {self.max_speed} km/s")


# Örnek kullanım
suv_arac = SUV("Toyota", "Land Cruiser", 2022, True)
spor_araba = SportCar("Ferrari", "488 GTB", 2021, 330)

print("SUV Aracı Özellikleri:")
suv_arac.display_info()

print("\nSpor Araba Özellikleri:")
spor_araba.display_info()
