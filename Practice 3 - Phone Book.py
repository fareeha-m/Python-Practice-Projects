# Contact List Storage and Retrieval

contact = {}

while True:
    print ("----Contact Lists----")
    print ("1. Add a New Contact")
    print ("2. Search Contact List")
    print ("3. Exit")

    choice = (input("Enter your choice: "))

    if choice == "1":
        name = (input("Enter Full Name: "))
        phone = (input("Enter Phone Number: "))
        contact[name]= phone
        print (f"Contact: {name} = {phone} has been added successfully.")
    
    elif choice == "2":
        search = (input("Enter the Name: "))
        if search in contact:
            print (f"{search}'s phone number is: {contact[search]}")
        else:
            print ("Contact not found!")
    elif choice == "3":
        print ("Program Exiting...")
        break
    else:
        print("End!")