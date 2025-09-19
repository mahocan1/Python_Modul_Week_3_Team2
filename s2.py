class Okul:
    def __init__(self, isim, kuruluş_yılı):
        self.isim = isim
        self.kuruluş_yılı = kuruluş_yılı
        self.öğrenciler = []  # öğrencileri sözlük olarak tutacağız: {"isim": ..., "sınıf": ...}
        self.öğretmenler = []  # öğretmenleri sözlük olarak tutacağız: {"isim": ..., "branş": ...}

    def add_new_student(self, student_name, sınıf):
        yeni_öğrenci = {"isim": student_name, "sınıf": sınıf}
        self.öğrenciler.append(yeni_öğrenci)
        print(f"{student_name} adlı öğrenci {sınıf} sınıfına eklendi.")

    def add_new_teacher(self, teacher_name, branch):
        yeni_öğretmen = {"isim": teacher_name, "branş": branch}
        self.öğretmenler.append(yeni_öğretmen)
        print(f"{teacher_name} adlı öğretmen {branch} branşına eklendi.")

    def view_student_list(self):
        if not self.öğrenciler:
            print("Henüz öğrenci yok.")
        else:
            print(f"{self.isim} Okulundaki Öğrenciler:")
            for öğrenci in self.öğrenciler:
                print(f"- {öğrenci['isim']} ({öğrenci['sınıf']} sınıfı)")

    def view_teacher_list(self):
        if not self.öğretmenler:
            print("Henüz öğretmen yok.")
        else:
            print(f"{self.isim} Okulundaki Öğretmenler:")
            for öğretmen in self.öğretmenler:
                print(f"- {öğretmen['isim']} ({öğretmen['branş']} öğretmeni)")


# Okul oluşturma
okul = Okul("Hilversum Anadolu Lisesi", 1998)

# Öğrenci ekleme
okul.add_new_student("Ahmet Yılmaz", "10A")
okul.add_new_student("Ayşe Demir", "9B")

# Öğretmen ekleme
okul.add_new_teacher("Mehmet Kaya", "Matematik")
okul.add_new_teacher("Fatma Koç", "Fizik")

# Listeleri görüntüleme
okul.view_student_list()
okul.view_teacher_list()
