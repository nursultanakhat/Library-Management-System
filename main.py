from library import Library

lib = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add book")
    print("2. Show books")
    print("3. Register user")
    print("4. Search book")
    print("5. Save data")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")

        lib.add_book(title, author)

        print("Book added successfully!")

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        name = input("Enter user name: ")

        lib.register_user(name)

    elif choice == "4":
        keyword = input("Enter title or author: ")

        lib.search_book(keyword)

    elif choice == "5":
        lib.save()

        print("Data saved successfully!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")