from datetime import date

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title 
        self.author = author
        self.year = year

    def info(self) -> None:
        print(f"Книга {self.title} , автора {self.author}, {self.year}")
    
    def is_old(self) -> bool:
        return date.today().year - self.year > 50


def main() -> None:
    book1 = Book("Война и мир", "Лев Толстой", 1867)
    book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
    book3 = Book("Современная книга", "Автор", 2000)

    book1.info()
    print("Старая книга?", book1.is_old())

    book3.info()
    print("Старая книга?", book3.is_old())
    book1.info()
    book2.info()


if __name__ == "__main__":
    main()