student = []
course = []
mark = []
m1 = {}

def getInforstudent():
    stu_id = input("Student ID: ")
    stu_name = input("Student name: ")
    stu_Dob = input("Student date of birth: ")
    return{"stu_id": stu_id,"stu_name": stu_name, "stu_Dob": stu_Dob }

def getCourse():
    cid = input("ID course: ")
    cname = input("Course name: ")
    return{"cid": cid, "cname": cname}

def getScore():
    for c in course:
        print(f'Enter marks for students in {c["cname"]} :')
        for s in student:
            score = float(input(f'{s["stu_name"]} :'))
            m1 = {'ID Course': c["cid"],'ID': s["stu_id"],'Mark' : score}
            mark.append(m1)

def printStudent():
    print("\nList of students:")
    for s in student:
        print(f'ID: {s["stu_id"]},  Name: {s["stu_name"]},  Date of Birth: {s["stu_Dob"]}')

def printCourse():
    print("\nList of courses:")
    for c in course:
        print(f'ID Course: {c["cid"]},  Course: {c["cname"]}')

def printScore():
    print("\nList of scores:")
    for s in student:
        print(f'ID: {s["stu_id"]},  Name: {s["stu_name"]},  Date of Birth: {s["stu_Dob"]}')
        for c in course:
            for m in mark:
                if m["ID Course"] == c["cid"] and m["ID"] == s["stu_id"]:
                    score = m["Mark"]
                    print(f'    ID Course: {c["cid"]}, Course: {c["cname"]}, Mark: {score} ')

n = int(input("Number of students: "))
for i in range(n):
    print('Student ' + str(i+1) +':')
    s = getInforstudent()
    student.append(s)
    
k = int(input("Number of course: "))
for i in range(k):
    print('Course ' + str(i+1) +':')
    c = getCourse()
    course.append(c)

getScore()

while True:
    print('\n 1. Print list of students')
    print(' 2. Print list of courses')
    print(' 3. Print list of scores')
    print(' 4. Exit')

    choice = int(input('Your choice: '))
    if choice == 1:
        printStudent()
    elif choice == 2:
        printCourse()
    elif choice == 3:
        printScore()
    elif choice == 4:
        break
    else:
        print("Invalid input. Please try again!")