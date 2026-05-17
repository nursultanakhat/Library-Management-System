from library import Library

lib = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add book")
    print("2. Show books")
    print("3. Register user")
    print("4. Search book")
    print("5. Remove book")
    print("6. Borrow book")
    print("7. Return book")
    print("8. Save data")
    print("9. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        lib.add_book(title, author)

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        lib.register_user(name, email)

    elif choice == "4":
        keyword = input("Enter title or author: ")
        lib.search_book(keyword)

    elif choice == "5":
        title = input("Enter book title to remove: ")
        lib.remove_book(title)

    elif choice == "6":
        title = input("Enter book title to borrow: ")
        lib.borrow_book(title)

    elif choice == "7":
        title = input("Enter book title to return: ")
        lib.return_book(title)

    elif choice == "8":
        lib.save()
        print("Data saved successfully!")

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")