import json

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        self.books.append({
            "title": title,
            "author": author
        })

    def show_books(self):
        if len(self.books) == 0:
            print("No books in library.")

        else:
            for book in self.books:
                print(book)

    def register_user(self, name):
        self.users.append(name)
        print("User registered successfully!")

    def search_book(self, keyword):
        found = False

        for book in self.books:
            if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
                print(book)
                found = True

        if not found:
            print("Book not found.")

    def save(self):
        with open("data.json", "w") as f:
            json.dump(self.books, f)