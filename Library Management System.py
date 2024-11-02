#Library Management System

lib = {}

while True:
    print ("----- Library Management System -----")
    print ("1. Add New Book")
    print ("2. Search Book")
    print ("3. Borrow a Book")
    print ("4. Retun a Book")
    print ("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input ("Enter the title of the book: ")
        author = input ("Enter the author's name: ")
        quantity = int(input("Enter the quantity: "))

        lib[title] = { 'author': author , 'quantity': quantity}
        print (f"{quantity} number of copies of the book {title} by {author} have been added.")
    
    elif choice == "2":
        search = input("Enter the title: ")
        
        if search in lib:
            print (f"{title} by {author} is available. Quantity = {quantity}")
        else:
            print ("Title not found!")
    elif choice == "3":
        title = input("Enter the title you want to borrow: ")
        if title in lib and lib[title]['quantity'] > 0:
            lib[title]['quantity'] -= 1
            print (f"The {title} has been issued to you")
        else:
            print ("Book not available")
    elif choice == "4":
        title = str(input("Enter the title you want to return: "))
        if title in lib:
            lib[title]['quantity'] +=1
            print (f"{title} has been added to the database.")
        else:
            print ("Enter the correct title!")
    elif choice == "5":
        print ("Exiting...")
        break
    else:
        print("Enter a valid choice!")

