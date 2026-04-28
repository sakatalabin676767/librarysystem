try:
    f = open("library.txt", "x")
    print("File created successfully!")
    with open("library.txt", "w") as f:
        f.write("ArtApp book ni Sir Ramir Sonsona")
except FileExistsError:
    print("File already exists!")

def addbook(): # student B
    print("---Add Book---")
    title = input("Enter book title: ")
    with open("library.txt", "a") as f:
        f.write(title + "\n")
    print("Book added successfully!")

def showbooks(): # student C
    with open("library.txt", "r") as f:
        books = f.read()
        print(books)
        
while True:
    print("1. Add Book") # student B
    print("2. Show Books") # student C 
    print("3. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!")

    if choice == 1:
        addbook()
    elif choice == 2:
        showbooks()
    elif choice == 3:
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice!")
