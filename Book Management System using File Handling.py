# Book Management System using File Handling

file_name = "books.txt"

while True:
    print("\n===== BOOK MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        file = open(file_name, "a")
        file.write(book_id + "," + book_name + "," + author + "\n")
        file.close()

        print("Book added successfully!")

    # View Books
    elif choice == "2":
        try:
            file = open(file_name, "r")
            data = file.readlines()

            if len(data) == 0:
                print("No books found.")
            else:
                print("\nBook Records:")
                for line in data:
                    details = line.strip().split(",")
                    print("ID:", details[0],
                          "| Name:", details[1],
                          "| Author:", details[2])

            file.close()

        except FileNotFoundError:
            print("File does not exist.")

    # Search Book
    elif choice == "3":
        search_id = input("Enter Book ID to search: ")

        try:
            file = open(file_name, "r")
            found = False

            for line in file:
                details = line.strip().split(",")

                if details[0] == search_id:
                    print("\nBook Found")
                    print("Book ID:", details[0])
                    print("Book Name:", details[1])
                    print("Author:", details[2])
                    found = True
                    break

            if found == False:
                print("Book not found.")

            file.close()

        except FileNotFoundError:
            print("File does not exist.")

    # Update Book
    elif choice == "4":
        update_id = input("Enter Book ID to update: ")

        try:
            file = open(file_name, "r")
            records = file.readlines()
            file.close()

            file = open(file_name, "w")
            found = False

            for line in records:
                details = line.strip().split(",")

                if details[0] == update_id:
                    new_name = input("Enter New Book Name: ")
                    new_author = input("Enter New Author Name: ")

                    file.write(update_id + "," + new_name + "," + new_author + "\n")
                    found = True
                else:
                    file.write(line)

            file.close()

            if found:
                print("Book updated successfully!")
            else:
                print("Book not found.")

        except FileNotFoundError:
            print("File does not exist.")

    # Remove Book
    elif choice == "5":
        remove_id = input("Enter Book ID to remove: ")

        try:
            file = open(file_name, "r")
            records = file.readlines()
            file.close()

            file = open(file_name, "w")
            found = False

            for line in records:
                details = line.strip().split(",")

                if details[0] == remove_id:
                    found = True
                else:
                    file.write(line)

            file.close()

            if found:
                print("Book removed successfully!")
            else:
                print("Book not found.")

        except FileNotFoundError:
            print("File does not exist.")

    # Exit
    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")