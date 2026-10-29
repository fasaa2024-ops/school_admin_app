students = []
while True:
    print("\n--- SCHOOL ADMIN APP ---")
    print("1. Add a new student")
    print("2. View all student")
    print("3. Exit")

    choice= input("Choose option(1,2,3): ")
    if choice == "1":
        name = input("enter student name: ")
        age =  input("enter student age: ")
        class_name = input("enter class: ")


        new_student = {
            "name": name,
            "age" : age,
            "class": class_name
        }
        students.append(new_student)
        print(f"{name} has been added! ")

    elif choice == "2":
        print("\n--- ALL STUDENTS ---")

        if len(students) ==0:
            print("no students in the register")
        else:
            for student in students:
                print(students)
                
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("invalid choice please enter 1,2 or 3")
    

