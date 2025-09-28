#small college wants max students of 8 along with details and courses
Max=8
#courses like CS, ECE, IT, MECH, CIVIL
Avail_courses=["CS","ECE","IT","MECH","CIVIL"]
#empty list
students=[]

 #ADD STUDENTS FUNCTIONS ------------ step 2
def add_student(students):
    if len(students) >= Max:
        print("only 8 students")
        return
    
    #using try-except to handle
    try:
        sid=int(input("enter the ID:"))
        name=input("enter the name:")
        course=input("course name(CS, ECE, IT, MECH, CIVIL):").upper()
        marks=int(input("enter marks:"))  #conversion of marks into integers 
        
        if course not in Avail_courses:
            print("invalid courses")
            return
        #Append dictionary to the list
        students.append({"id":sid, "name":name, "course":course, "marks":marks})
        print("STUDENT SUCCESSFULLY ADDED")

    except ValueError:
        print("invalid, better luck next time")

#VIEW STUDENTS FUNCTION --------------- step 3
def view_student(students):
    if not students:
        print("no student ")
    else:
        print("\n-----STUDENTS DATABASE-------") #table creation 
        print("\n+--------+-------------------+------------+---------")
        print("{:<5} {:<15} {:<10} {:<5}".format("SID", "SName","Course","Marks")) 
        #.format is used to insert the value into str and {:<3} ==> represents the left align which gives the whitespace and can be represent in table format
        print("\n-------------------------------------------------------------------")
        for i in students:
            print("{:<5} {:<15} {:<10} {:<5}".format(i["id"], i["name"], i["course"],i["marks"]))
            print()

#STUDENT SEARCH
def search_student(students):
    x=input("enter the Id or name:")
    found=False #assuming that 
    for i in students: 
        if str(i["id"]) ==  x or i["name"].lower()==x.lower(): #here for id givven str because it converting the int to str
            print(f" details: ID={i['id']}, Name={i['name']}, Course={i['course']}, Marks={i['marks']}") #Double quotes inside f-string will break it. use single quotes
            found=True
            break # to stop for searching for the candidate
    if not found:
        print("Oops! candidate not found")

#STUDENT UPDATE  USING TRY-EXCEPT 
def update_student(students):
    try:
        sid=int(input("enter the ID to update:"))
        for i in students:
            if i["id"]==sid:
                print("1.Update Course:")
                print("2.Update Marks:")
                choice=input("enter the choice:")
                if choice=="1":
                    new_course=input("enter the course:").upper()
                    if new_course in Avail_courses:
                        i["course"]=new_course #= assignment
                        print("course update")
                    else:
                        print("not updated yet")
                elif choice=="2":
                    new_marks=int(input("enter the marks:"))
                    i["marks"]=new_marks
                    print("marks updated")
                    return
                print("id not found")
    except ValueError:
        print("invalid, try again")

#FUNCTION TO DELETE STUDENT
def delete_student(students):
    try:
        sid=int(input("enter the id to delete: "))
        for i in students:
            if i["id"] == sid:
                students.remove(i)
                print("student deleted")
                return
        print("student ID not found")
    except ValueError:
        print()