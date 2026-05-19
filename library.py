import json
import os

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called.")
        return func(*args, **kwargs)
    return wrapper


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()

    @log_action
    def add_book(self, title, author):
        self.books.append({
            "title": title,
            "author": author,
            "status": "available"
        })

        print("Book added successfully!")

    @log_action
    def show_books(self):
        if len(self.books) == 0:
            print("No books in library.")

        else:
            for book in self.books:
                print(book)

    @log_action
    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)

                print("Book removed successfully!")
                return

        print("Book not found.")

    @log_action
    def register_user(self, name, email):
        self.users.append({
            "name": name,
            "email": email
        })

        print("User registered successfully!")

    @log_action
    def search_book(self, keyword):
        found = False

        for book in self.books:
            if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
                print(book)
                found = True

        if not found:
            print("Book not found.")

    @log_action
    def borrow_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():

                if book["status"] == "available":
                    book["status"] = "borrowed"
                    print("Book borrowed successfully!")

                else:
                    print("This book is already borrowed.")

                return

        print("Book not found.")

    @log_action
    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():

                if book["status"] == "borrowed":
                    book["status"] = "available"
                    print("Book returned successfully!")

                else:
                    print("This book was not borrowed.")

                return

        print("Book not found.")

    @log_action
    def save(self):
        data = {
            "books": self.books,
            "users": self.users
        }

        try:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

            print("Data saved successfully!")

        except Exception as e:
            print("Error while saving:", e)

    def load_data(self):
        if os.path.exists("data.json"):

            try:
                with open("data.json", "r") as f:
                    data = json.load(f)

                    self.books = data.get("books", [])
                    self.users = data.get("users", [])

            except:
                print("Error loading data.")