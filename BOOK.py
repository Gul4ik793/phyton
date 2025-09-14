class Book:
    def __init__(self, name, autor, ISBN, status):
        self.name = name
        self.autor = autor
        self.ISBN= ISBN
        self.status = status

    def change_status(self, status):
        self.status = status
        return self.status


class Library:
    def __init__(self, name):
        self.name = name
        self.list_books = list()

    def add_list_book(self, book):
        self.list_books.append(book)

    def get_books(self):
       return [[book.name, book.autor, book.ISBN, book.status] for book in self.list_books]

    def get_book_name(self, name):
        for book in self.list_books:
            if book.name == name:
                return "Книга в библиотеке есть со статусом:", book.status
        return False


    def book_change_status(self, book, status):
        if book in self.list_books:
            book.status = status
        else:
            return "книги нет в библиотеке"

book_one = Book("Первая книга", "Автор 1", "1", "в наличии")
book_two = Book("Вторая книга", "Автор 2", "2", "в наличии")

library = Library("Библиотека")
library.add_list_book(book_one)
library.add_list_book(book_two)

print("Список книг в Библиотеке до изменения статусов выдачи: ", library.get_books())
print("Изменила статус книги 'Вторая книга' на 'выдана': ", book_two.change_status("выданa"))

library.book_change_status(book_one, "выдана")
print("Выдала книгу 'Вторая книга'")

print("Список книг в Библиотеке со статусами после изменения статуса: ", library.get_books())

print(F"Ищем в библиотеке книгу :", library.get_book_name("Вторая книга"))


