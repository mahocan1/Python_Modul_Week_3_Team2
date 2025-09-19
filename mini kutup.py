import json
import os


# ========== Kitap Sınıfları ==========
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False
        self.borrowed_by = None

    def show_info(self):
        status = f"Ödünçte ({self.borrowed_by})" if self.is_borrowed else "Müsait"
        print(f"{self.title} - {self.author} ({self.publication_year}) | Durum: {status}")

    def borrow(self, user):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user.name
            user.borrowed_books.append(self.title)
            print(f"{self.title} başarıyla ödünç alındı.")
        else:
            print(f"{self.title} zaten ödünç alınmış!")

    def return_book(self, user):
        if self.is_borrowed and self.borrowed_by == user.name:
            self.is_borrowed = False
            self.borrowed_by = None
            user.borrowed_books.remove(self.title)
            print(f"{self.title} başarıyla iade edildi.")
        else:
            print("Bu kitabı iade edemezsiniz!")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by,
            "type": "Book"
        }


class Novel(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def to_dict(self):
        data = super().to_dict()
        data["genre"] = self.genre
        data["type"] = "Novel"
        return data


class Magazine(Book):
    def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue

    def to_dict(self):
        data = super().to_dict()
        data["issue"] = self.issue
        data["type"] = "Magazine"
        return data


# ========== Kullanıcı Sınıfı ==========
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.borrowed_books = []

    def borrow_book(self, book):
        book.borrow(self)

    def return_book(self, book):
        book.return_book(self)

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("Henüz ödünç alınmış kitabınız yok.")
        else:
            print("Ödünç alınan kitaplar:")
            for title in self.borrowed_books:
                print(f"- {title}")

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": self.borrowed_books
        }


# ========== Kütüphane Sınıfı ==========
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def show_all_books(self):
        if not self.books:
            print("Kütüphanede hiç kitap yok.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. ", end="")
                book.show_info()

    def login(self, name, password):
        for user in self.users:
            if user.name == name and user.password == password:
                print(f"Hoşgeldiniz, {name}!")
                return user
        print("Kullanıcı adı veya şifre hatalı.")
        return None

    def save(self, file):
        data = {
            "name": self.name,
            "books": [book.to_dict() for book in self.books],
            "users": [user.to_dict() for user in self.users]
        }
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("📁 Veriler kaydedildi.")

    def load(self, file):
        if not os.path.exists(file):
            return
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.name = data["name"]

        # Kitapları geri yükle
        self.books = []
        for b in data["books"]:
            if b["type"] == "Novel":
                book = Novel(b["title"], b["author"], b["publication_year"], b["genre"])
            elif b["type"] == "Magazine":
                book = Magazine(b["title"], b["author"], b["publication_year"], b["issue"])
            else:
                book = Book(b["title"], b["author"], b["publication_year"])
            book.is_borrowed = b["is_borrowed"]
            book.borrowed_by = b["borrowed_by"]
            self.books.append(book)

        # Kullanıcıları geri yükle
        self.users = []
        for u in data["users"]:
            user = User(u["name"], u["password"])
            user.borrowed_books = u["borrowed_books"]
            self.users.append(user)


# ========== Ana Program ==========
def main():
    lib = Library("Merkez Kütüphane")
    lib.load("library.json")

    # Örnek veri ekleyelim (ilk açılışta)
    if not lib.books:
        lib.add_book(Novel("Sefiller", "Victor Hugo", 1862, "Dram"))
        lib.add_book(Magazine("Bilim Dergisi", "TÜBİTAK", 2023, "Ekim"))
        lib.add_book(Book("Python 101", "Guido van Rossum", 1991))

    while True:
        print("\n=== Kütüphane Yönetim Sistemi ===")
        print("1 - Giriş Yap")
        print("2 - Kayıt Ol")
        print("3 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            name = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            user = lib.login(name, password)
            if user:
                while True:
                    print("\n--- Menü ---")
                    print("1 - Tüm kitapları listele")
                    print("2 - Kitap ödünç al")
                    print("3 - Kitap iade et")
                    print("4 - Ödünç aldığım kitaplar")
                    print("5 - Kaydet ve çık")
                    choice = input("Seçiminiz: ")

                    if choice == "1":
                        lib.show_all_books()
                    elif choice == "2":
                        lib.show_all_books()
                        idx = int(input("Kaç numaralı kitabı ödünç almak istiyorsunuz? ")) - 1
                        if 0 <= idx < len(lib.books):
                            user.borrow_book(lib.books[idx])
                    elif choice == "3":
                        user.list_borrowed_books()
                        title = input("İade etmek istediğiniz kitabın adı: ")
                        for book in lib.books:
                            if book.title == title:
                                user.return_book(book)
                                break
                        else:
                            print("Böyle bir kitabınız yok.")
                    elif choice == "4":
                        user.list_borrowed_books()
                    elif choice == "5":
                        lib.save("library.json")
                        return
                    else:
                        print("Geçersiz seçim.")

        elif secim == "2":
            name = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            lib.add_user(User(name, password))
            print("Kullanıcı başarıyla oluşturuldu.")

        elif secim == "3":
            lib.save("library.json")
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
