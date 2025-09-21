class Dikdortgen():
    def __init__(self, kisa_kenar, uzun_kenar):
        self.kisa_kenar = kisa_kenar
        self.uzun_kenar = uzun_kenar

    def alan(self):
        return self.kisa_kenar * self.uzun_kenar

    def cevre(self):
        return 2 * (self.kisa_kenar + self.uzun_kenar)
    

dikdortgen1 = Dikdortgen(5, 10)
print("Dikdörtgenin alanı:", dikdortgen1.alan())


print("Dikdörtgenin cevresi:", dikdortgen1.cevre())

    