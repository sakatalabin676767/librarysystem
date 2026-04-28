try:
    f = open("library.txt", "x")
    print("File created successfully!")
    with open("library.txt", "w") as f:
        f.write("ArtApp book ni Sir Ramir Sonsona")
except FileExistsError:
    print("File already exists!")

def addbook(): # student B
    pass # kamo na edit ani (remove ang pass)

def showbooks(): # student C
    pass # kani sad (remove ang pass)
        
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
