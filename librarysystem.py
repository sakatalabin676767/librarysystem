try:
    f = open("library.txt", "x")
    print("File created successfully!")
    with open("library.txt", "w") as f:
        f.write("ArtApp book ni Sir Ramir Sonsona")
except FileExistsError:
    print("File already exists!")

def addbook():
    print("---Add Book---")
    title = input("Enter book title: ")
    with open("library.txt", "a") as f:
        f.write(title + "\n")
    print("Book added successfully!")

def showbooks():
    with open("library.txt", "r") as f:
        books = f.read()
        print(books)

def updatebooks():
    with open("library.txt", 'r') as f:
        content = f.read()
        old_text = input("\nEnter book to update: ")
    new_text = input("Enter updated book: ")
    new_content = content.replace(old_text, new_text)
    with open("library.txt", 'w') as f:
        f.write(new_content)
    print("Book Updated Successfully!\n")

def searchbook():
    with open("library.txt", 'r') as f:
        content = f.read()
    textfind = input("Search for book: ")
    if textfind in content:
        print("Book found!)

while True:
    print("1. Add Book")
    print("2. Show Books")
    print("3. Update Book")
    print("4. Search Book")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!")

    if choice == 1:
        addbook()
    elif choice == 2:
        showbooks()
    elif choice == 3:
        updatebooks()
    elif choice == 4:
        searchbook()
    elif choice == 5:
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice!")