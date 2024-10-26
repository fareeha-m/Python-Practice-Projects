# Student Grade Management System
print ("----Student Grade Management System-----")

students = {}

while True:
    print ("1. Add New")
    print ("2. Search")
    print ("3. Display Full Data")
    print ("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Full Name: ")
        score = int(input ("Enter marks obtained out of 100: "))
        students[name] = score      #to save data
        print (f"{name} obtained {score} out of 100. Data Saved")

    elif choice == "2":
        search = str(input("Enter Full Name: ")).strip()
        if search in students:
            print (f"The score of {search} out of 100 is {score}")
        else:
            print ("Data Not Found!")
    elif choice == "3":
        if students:
            print ("---- Student Data ----")
            for name, score in students.items():
                print (f"{name} = {score} out of 100")
        else:
            print ("No Data Found!")
    elif choice == "4":
        print ("Exiting...")
        break
    else:
        print ("Enter a valid number!")







