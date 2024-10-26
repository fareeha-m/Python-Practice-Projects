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

        if 90 <= score <= 100:
            grade = "A"
        elif 80 <= score < 90:
            grade = "B"
        elif 70 <= score < 80:
            grade = "C"
        elif 60 <= score < 70:
            grade = "D"
        elif score < 60:
            grade = "F"
        else:
            print ("Enter valid score!")
            continue

        students[name] = {'score' : score , 'grade' : grade }      #to save data
        print (f"{name} obtained {score} out of 100 and the grade is {grade}. Data Saved!")

    elif choice == "2":
        search = str(input("Enter Full Name: ")).strip()
        if search in students:
            print (f"The score of {search} out of 100 is {score} and the grade is {grade}")
        else:
            print ("Data Not Found!")
    elif choice == "3":
        if students:
            print ("----- Student Grade Record -----")
            for name, info in students.items():
                print (f"{name} = {info['score']}/100 | grade = {info['grade']}.")
        else:
            print ("No Data Found!")
    elif choice == "4":
        print ("Exiting...")
        break
    else:
        print ("Enter a valid number!")







