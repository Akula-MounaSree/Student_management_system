#Main menu
from functions import add_student, view_student, search_student, update_student, delete_student

def menu():
    students=[] #empty list to store students
    while True:
        print("\n======STUDENT MANAGEMENT SYSTEM========")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice=input("enter the choice:")

        if choice=="1":
            add_student(students)
        elif choice=="2":
            view_student(students)
        elif choice=="3":
            search_student(students)
        elif choice=="4":
            update_student(students)
        elif choice=="5":
            delete_student(students)
        elif choice=="6":
            print("okie dokie... Bye!")
            break
        else:
            print("invalid input")
#direct calling            
menu()  