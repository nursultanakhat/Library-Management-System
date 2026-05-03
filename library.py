import json

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def show_books(self):
        for book in self.books:
            print(book)

    def save(self):
        with open("data.json", "w") as f:
            json.dump(self.books, f)