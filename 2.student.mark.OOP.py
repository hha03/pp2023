student = []
course = []
mark = []
m1 = {}

class Student:
    def __init__(self, sid, sname, sDob):
        self.__sid = sid
        self.__sname = sname
        self.__sDob = sDob

    def get_sid(self):
        return self.__sid
    def get_sname(self):
        return self.__sname
    def get_sDob(self):
        return self.__sDob

    def student(self):
        sid = self.__sid
        sname = self.__sname
        sDob = self.__sDob
        print('ID:',sid , ', Name:',sname, ', DOB:',sDob)

class Course:
    def __init__(self, cid, cname):
        self.__cid = cid
        self.__cname = cname

    def get_cid(self):
        return self.__cid
    def get_cname(self):
        return self.__cname

    def course(self):
        cid = self.__cid
        cname = self.__cname
        print('ID Course:',cid , ', Course:',cname)

class Score:
    def __init__(self, score):
        self.__score= score

    def get_score(self):
        return self.__score

def getInforstudent():
    stu_id = input("Student ID: ")
    stu_name = input("Student name: ")
    stu_Dob = input("Student date of birth: ")
    stu = Student(stu_id, stu_name, stu_Dob)
    student.append(stu)

def getCourse():
    cid = input("ID course: ")
    cname = input("Course name: ")
    lsco = Course(cid, cname)
    course.append(lsco)

def getScore():
    for c in course:
        print(f'Enter marks for students in {c.get_cname()} :')
        for s in student:
            score = float(input(f'{s.get_sname()} :'))
            m1 = Score(score)
            m1 = {'ID Course': c.get_cid(),'ID': s.get_sid(),'Mark' : score}
            mark.append(m1)

def printStudent():
    print("\nList of students:")
    for s in student:
        s.student()

def printCourse():
    print("\nList of courses:")
    for c in course:
        c.course()

def printScore():
    print("\nList of scores:")
    for s in student:
        print(f'\nID: {s.get_sid()},  Name: {s.get_sname()},  Date of Birth: {s.get_sDob()}')
        for c in course:
            for m in mark:
                if m['ID Course'] == c.get_cid() and m['ID'] == s.get_sid():
                    score = m['Mark']
                    print(f'    ID Course: {c.get_cid()}, Course: {c.get_cname()}, Mark: ',score)

n = int(input("Number of students: "))
for i in range(n):
    print(f'Student {i+1}: ')
    s = getInforstudent()

k = int(input("Number of course: "))
for i in range(k):
    print(f'Course {i+1}: ' )
    c = getCourse()

getScore()

while True:
    print('\n1.Print list of students')
    print('2.Print list of courses')
    print('3.Print list of scores')
    print('4.Exit')
    choice = int(input('Enter your choice: '))
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
