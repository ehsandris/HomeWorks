# Library catalog stored as a dictionary
books = {
    "1984": "George Orwell",
    "The Hobbit": "J.R.R. Tolkien",
    "Pride and Prejudice": "Jane Austen",
    "The Alchemist": "Paulo Coelho",
    "Crime and Punishment": "Fyodor Dostoevsky"
}


while True:

    user_choice = input("""
Library Management System

1. Add Book
2. Search Book
3. Show All Books
4. Exit

Enter your choice: 
""").strip()

    # Add a new book
    if user_choice == "1":

        book_title = input(
            "Enter book title: "
        ).strip()

        if book_title in books:

            print(
                f"Book already exists:\n"
                f"{book_title} --> {books[book_title]}"
            )

        else:

            author_name = input(
                "Enter author name: "
            ).strip()

            books[book_title] = author_name

            print(
                "Book added successfully."
            )

    # Search for a book
    elif user_choice == "2":

        book_title = input(
            "Enter book title: "
        ).strip()

        if book_title in books:

            print(
                f"Book found:\n"
                f"{book_title} --> {books[book_title]}"
            )

        else:

            print("Book not found.")

    # Display all books
    elif user_choice == "3":

        if books:

            print("\nLibrary Catalog")
            print("----------------")

            for book_title, author_name in books.items():
                print(
                    f"{book_title} --> {author_name}"
                )

        else:

            print("No books available.")

    # Exit program
    elif user_choice == "4":

        print("Goodbye!")
        break

    # Invalid input
    else:

        print(
            "Invalid choice. "
            "Please select a number between 1 and 4."
        )