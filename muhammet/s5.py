# Müşteri sınıfı
class Musteri:
    def __init__(self, isim, soyad, tc_identification, telefon):
        self.isim = isim
        self.soyad = soyad
        self.tc_identification = tc_identification
        self.telefon = telefon

    def display_information(self):
        print(f"Müşteri Bilgileri:\n"
              f"Ad: {self.isim}\n"
              f"Soyad: {self.soyad}\n"
              f"TC: {self.tc_identification}\n"
              f"Telefon: {self.telefon}")


# Hesap sınıfı (Müşteri'den miras alıyor)
class Hesap(Musteri):
    def __init__(self, isim, soyad, tc_identification, telefon, hesap_numarasi, bakiye=0):
        super().__init__(isim, soyad, tc_identification, telefon)
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def deposit(self, amount):
        self.bakiye += amount
        print(f"{amount} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def money_check(self, amount):
        if self.bakiye >= amount:
            self.bakiye -= amount
            print(f"{amount} TL çekildi. Kalan bakiye: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye! İşlem gerçekleştirilemedi.")

    def display_balance(self):
        print(f"Hesap Numarası: {self.hesap_numarasi} | Güncel Bakiye: {self.bakiye} TL")


# Müşteri oluşturma
musteri1 = Hesap("Ahmet", "Yılmaz", "12345678901", "0555 111 22 33", "TR100200300", 500)

# Müşteri bilgilerini görüntüleme
musteri1.display_information()

# Hesap işlemleri
musteri1.display_balance()
musteri1.deposit(200)
musteri1.money_check(100)
musteri1.money_check(700)  # Yetersiz bakiye durumu
musteri1.display_balance()
