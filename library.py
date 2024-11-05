library = []

balance = 150

books = {
    'Clean Code': 35,
    'Clean Coder': 50,
    'Grokking Algorithms': 85,
    'Easy Matpolib': 65, 
}


def add_book_to_library():
    global balance
    name = input("Enter the title of the book: ")
    if name in books:
        # price = key
        price = books[name]
        if balance >= price:
            # append book to library & delete from books
            library.append(name)
            del books[name]
            balance -= price
        else:
            print("Not enough money.")
    else:
        print(f"Book {name} not found.")
    print('-------------------------')
    


def remove_book_from_library():
    name = input("Enter the title of the book you want to remove: ")
    if name in library:
        library.remove(name)
        print(f"Book '{name}' removed from your library.")
    else:
        print(f"Book {name} not found.")
    print('-------------------------')



def view_books_shop():
    if books:
        print(books)
    else:
        print("Shop is empty")
    print('-------------------------')


def view_library():
    if library:
        print(library)
    else:
        print("Library is empty")
    print('-------------------------')


def view_balance():
    # print balance
    print(f"Your balance: ${balance}")


actions = {
    '1': add_book_to_library,
    '2': remove_book_from_library,
    '3': view_books_shop,
    '4': view_library,
    '5': view_balance
}

while True:
    print("1. Add book to library")
    print("2. Remove book from library")
    print("3. View books shop")
    print("4. View your library")
    print("5. View your balance")
    print("6. Leave")

    choice = input("Choose the action: ")

    if choice == 5:
        print('Bye')
        break
    elif choice in actions:
        actions[choice]()
    else:
        print("Syntax Error. undefind action.")