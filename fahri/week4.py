#1.Cevap
"""
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * height
        self.perimeter = self.width * 2 + self.height * 2

rectangle2 = Rectangle(5, 7)
print("area of ​​the rectangle:" , rectangle2.area)
print("perimeter of the rectangle:", rectangle2.perimeter)
"""

#2.Cevap
"""
class Okul():
    def __init__(self, isim, kurulus_yili):
        self.isim = isim
        self.kurulus_yili = kurulus_yili
        self.ogrenciler = []
        self.ogretmenler = {}

    def yeni_ogrenci_ekle(self, ogrenci_adi,sinif):
        self.ogrenciler.append({"isim": ogrenci_adi , "sinif" : sinif})
        print(f"{ogrenci_adi} adlı öğrenci {sinif} sınıfına eklendi.")

    def yeni_ogretmen_ekle(self , ogretmen_adi, brans):
        self.ogretmenler[ogretmen_adi] = brans
        print(f"{ogretmen_adi} adlı öğretmen {brans} branşı ile eklendi.")
    
    def ogrenci_listesini_gor(self):
        if not self.ogrenciler:
            print("Henüz öğrenci yok")
        else:
            print("Ogrenci Listesi")
            for ogrenci in self.ogrenciler:
                print(f"- {ogrenci['isim']} (Sınıf: {ogrenci['sinif']})")

    def ogretmen_listesini_gor(self):
        if not self.ogretmenler:
            print("Henüz öğretmen yok")
        else:
            print("Ogretmen Listesi")
            for ogretmen,brans in self.ogretmenler.items():
                print(f"- {ogretmen} (Branş: {brans})")
            
def s2():



    okul1 = Okul("Beykoz Meslek Lisesi" , 1950)
    okul1.yeni_ogrenci_ekle("Ahmet", "8D")
    okul1.yeni_ogrenci_ekle("Mehmet", "9A")
    okul1.yeni_ogretmen_ekle("Fahri Hoca", "Fizik")
    okul1.yeni_ogretmen_ekle("Zeynep Hoca", "Biyoloji")

    okul1.ogrenci_listesini_gor()
    okul1.ogretmen_listesini_gor()

"""
"""
#3.Cevap

class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

class Dikdortgen(Sekil):
    def calculate_area(self):
        return self.genislik * self.yukseklik
class Kare(Sekil):
    def calculate_area(self):
        return self.genislik * self.yukseklik

dikdortgen = Dikdortgen(5, 3)  
kare = Kare(4, 4)             

print(f"Dikdörtgenin Alanı: {dikdortgen.calculate_area()}")
print(f"Karenin Alanı: {kare.calculate_area()}")


#4.Cevap
"""

"""
class Arac:
    def __init__(self, marka, model, yıl):
        self.marka = marka
        self.model = model
        self.yıl = yıl

    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yıl}"


class Arazi_araci(Arac):
    def __init__(self, marka, model, yıl, dortceker):
        super().__init__(marka, model, yıl) 
        self.dortceker = dortceker

    def __str__(self):
        return super().__str__() + f", Dört Çeker: {'Evet' if self.dortceker else 'Hayır'}"


class Spor_Araba(Arac):
    def __init__(self, marka, model, yıl, max_hız):
        super().__init__(marka, model, yıl)  # sadece 3 parametre gönder
        self.max_hız = max_hız

    def __str__(self):
        return super().__str__() + f", Maksimum Hız: {self.max_hız} km/s"
       

# Örnekler
arac1 = Arazi_araci("Toyota", "Land Cruiser", 2022, True)
arac2 = Spor_Araba("Ferrari", "488 GTB", 2021, 330)

print("Arazi Aracı Bilgileri:", arac1)
print("Spor Araba Bilgileri:", arac2)
print("Arazi Aracı:", arac1.dortceker)
print("Spor Aracın Max Hızı:", arac2.max_hız)
"""
#5.Cevap
"""
class Müsteri:
    def __init__(self, ad, soyad, tc, telefon):
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.telefon = telefon

    def display_information(self):
        print("----- Müşteri Bilgileri -----")
        print(f"Adı       : {self.ad}")
        print(f"Soyadı     : {self.soyad}")
        print(f"TC Kimlik Numarası  : {self.tc}")
        print(f"Telefon Numarası    : {self.telefon}")
    

    
class Hesap(Müsteri):
    def __init__(self, ad, soyad, tc, telefon, hesap_nu, bakiye=0):
        super().__init__(ad, soyad, tc, telefon)
        self.hesap_nu = hesap_nu
        self.bakiye = bakiye

    def deposit(self, miktar):
        self.bakiye+=miktar
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def money_check(self, miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")
        else:
            print("❌ Yetersiz bakiye! İşlem gerçekleştirilemedi.")

    def display_balance(self):
        print(f"Hesap No: {self.hesap_nu}, Güncel Bakiye: {self.bakiye} TL")


musteri1 = Müsteri("Ali", "Yılmaz", "12345678901", "0555 111 22 33")
hesap1 = Hesap("Ali", "Yılmaz", "12345678901", "0555 111 22 33", "TR100200300", 1000)

print("\n----- Hesap İşlemleri -----")
hesap1.display_balance()
hesap1.deposit(500)
hesap1.money_check(300)
hesap1.money_check(1500) 
hesap1.display_balance()

"""
"""
import json

# -----------------------------
# Kitap Sınıfları
# -----------------------------
class Kitap:
    def __init__(self, baslik, yazar, yayin_yili):
        self.baslik = baslik
        self.yazar = yazar
        self.yayin_yili = yayin_yili
        self.odunc_alindi_mi = False
        self.kim_odunc_aldi = None

    def bilgi_goster(self):
        durum = f"Ödünç alındı: {self.kim_odunc_aldi}" if self.odunc_alindi_mi else "Müsait"
        return f"{self.baslik} ({self.yazar}, {self.yayin_yili}) - {durum}"

    def odunc_al(self, kullanici):
        if not self.odunc_alindi_mi:
            self.odunc_alindi_mi = True
            self.kim_odunc_aldi = kullanici.ad
            kullanici.odunc_kitaplar.append(self.baslik)
            return True
        return False

    def iade_et(self, kullanici):
        if self.odunc_alindi_mi and self.kim_odunc_aldi == kullanici.ad:
            self.odunc_alindi_mi = False
            self.kim_odunc_aldi = None
            kullanici.odunc_kitaplar.remove(self.baslik)
            return True
        return False

    def to_dict(self):
        return {
            "tip": self.__class__.__name__,
            "baslik": self.baslik,
            "yazar": self.yazar,
            "yayin_yili": self.yayin_yili,
            "odunc_alindi_mi": self.odunc_alindi_mi,
            "kim_odunc_aldi": self.kim_odunc_aldi
        }


class Roman(Kitap):
    def __init__(self, baslik, yazar, yayin_yili, tur):
        super().__init__(baslik, yazar, yayin_yili)
        self.tur = tur

    def to_dict(self):
        data = super().to_dict()
        data["tur"] = self.tur
        return data


class Dergi(Kitap):
    def __init__(self, baslik, yazar, yayin_yili, sayi):
        super().__init__(baslik, yazar, yayin_yili)
        self.sayi = sayi

    def to_dict(self):
        data = super().to_dict()
        data["sayi"] = self.sayi
        return data


# -----------------------------
# Kullanıcı Sınıfı
# -----------------------------
class Kullanici:
    def __init__(self, ad, sifre):
        self.ad = ad
        self.sifre = sifre
        self.odunc_kitaplar = []

    def kitap_odunc_al(self, kitap):
        return kitap.odunc_al(self)

    def kitap_iade_et(self, kitap):
        return kitap.iade_et(self)

    def odunc_listesi(self):
        return self.odunc_kitaplar

    def to_dict(self):
        return {
            "ad": self.ad,
            "sifre": self.sifre,
            "odunc_kitaplar": self.odunc_kitaplar
        }


# -----------------------------
# Kütüphane Sınıfı
# -----------------------------
class Kutuphane:
    def __init__(self, ad):
        self.ad = ad
        self.kitaplar = []
        self.kullanicilar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kullanici_ekle(self, kullanici):
        self.kullanicilar.append(kullanici)

    def kitaplari_goster(self):
        for idx, kitap in enumerate(self.kitaplar, start=1):
            print(f"{idx}. {kitap.bilgi_goster()}")

    def giris_yap(self, ad, sifre):
        for kullanici in self.kullanicilar:
            if kullanici.ad == ad and kullanici.sifre == sifre:
                return kullanici
        return None

    def kaydet(self, dosya):
        data = {
            "kitaplar": [kitap.to_dict() for kitap in self.kitaplar],
            "kullanicilar": [k.to_dict() for k in self.kullanicilar]
        }
        with open(dosya, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def yukle(self, dosya):
        try:
            with open(dosya, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Kullanıcıları yükle
            self.kullanicilar = [Kullanici(u["ad"], u["sifre"]) for u in data.get("kullanicilar", [])]
            for i, u in enumerate(self.kullanicilar):
                u.odunc_kitaplar = data["kullanicilar"][i]["odunc_kitaplar"]

            # Kitapları yükle
            self.kitaplar = []
            for b in data.get("kitaplar", []):
                if b["tip"] == "Roman":
                    kitap = Roman(b["baslik"], b["yazar"], b["yayin_yili"], b.get("tur", ""))
                elif b["tip"] == "Dergi":
                    kitap = Dergi(b["baslik"], b["yazar"], b["yayin_yili"], b.get("sayi", ""))
                else:
                    kitap = Kitap(b["baslik"], b["yazar"], b["yayin_yili"])
                kitap.odunc_alindi_mi = b["odunc_alindi_mi"]
                kitap.kim_odunc_aldi = b["kim_odunc_aldi"]
                self.kitaplar.append(kitap)

        except FileNotFoundError:
            pass


# -----------------------------
# Program Akışı
# -----------------------------
def main():
    kutuphane = Kutuphane("Merkez Kütüphane")
    kutuphane.yukle("kutuphane.json")

    print("📚 KÜTÜPHANE SİSTEMİNE HOŞGELDİNİZ")

    # Giriş ekranı
    while True:
        secim = input("1- Giriş Yap\n2- Yeni Hesap Oluştur\nSeçiminiz: ")
        if secim == "1":
            ad = input("Kullanıcı adı: ")
            sifre = input("Şifre: ")
            kullanici = kutuphane.giris_yap(ad, sifre)
            if kullanici:
                print(f"✅ Hoş geldiniz, {kullanici.ad}")
                break
            else:
                print("❌ Hatalı kullanıcı adı veya şifre.")
        elif secim == "2":
            ad = input("Yeni kullanıcı adı: ")
            sifre = input("Şifre: ")
            kullanici = Kullanici(ad, sifre)
            kutuphane.kullanici_ekle(kullanici)
            print("✅ Hesap oluşturuldu, giriş yapıldı.")
            break
        else:
            print("Geçersiz seçim!")

    # Menü
    while True:
        print("\n----- MENÜ -----")
        print("1 - Tüm kitapları listele")
        print("2 - Kitap ödünç al")
        print("3 - Kitap iade et")
        print("4 - Ödünç aldığım kitaplar")
        print("5 - Kaydet ve çık")

        secim = input("Seçiminiz: ")

        if secim == "1":
            kutuphane.kitaplari_goster()

        elif secim == "2":
            kutuphane.kitaplari_goster()
            idx = int(input("Ödünç almak istediğiniz kitabın numarası: ")) - 1
            if 0 <= idx < len(kutuphane.kitaplar):
                if kullanici.kitap_odunc_al(kutuphane.kitaplar[idx]):
                    print("✅ Kitap ödünç alındı.")
                else:
                    print("❌ Kitap zaten ödünç alınmış.")
            else:
                print("❌ Geçersiz seçim.")

        elif secim == "3":
            if not kullanici.odunc_kitaplar:
                print("Ödünç aldığınız kitap yok.")
            else:
                for i, baslik in enumerate(kullanici.odunc_kitaplar, start=1):
                    print(f"{i}. {baslik}")
                idx = int(input("İade etmek istediğiniz kitabın numarası: ")) - 1
                if 0 <= idx < len(kullanici.odunc_kitaplar):
                    baslik = kullanici.odunc_kitaplar[idx]
                    kitap = next(b for b in kutuphane.kitaplar if b.baslik == baslik)
                    if kullanici.kitap_iade_et(kitap):
                        print("✅ Kitap iade edildi.")
                else:
                    print("❌ Geçersiz seçim.")

        elif secim == "4":
            if not kullanici.odunc_kitaplar:
                print("Ödünç aldığınız kitap yok.")
            else:
                print("📖 Ödünç aldığınız kitaplar:")
                for b in kullanici.odunc_kitaplar:
                    print("-", b)

        elif secim == "5":
            kutuphane.kaydet("kutuphane.json")
            print("💾 Veriler kaydedildi. Çıkılıyor...")
            break

        else:
            print("❌ Geçersiz seçim!")


if __name__ == "__main__":
    main()
"""