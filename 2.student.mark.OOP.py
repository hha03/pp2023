student = []
course = []
mark = []

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
    def get_course_ids(self):
        return self.__course_ids
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
    def __init__(self,course,student,score):
        self.__course = course
        self.__student = student
        self.__score= score
    
    def get_course(self):
        return self.__course
    def get_student(self):
        return self.__student
    def get_score(self):
        return self.__score
    def mark(self):
        course = self.__course
        student = self.__student
        score = self.__score
        print('Course:',course , ', Student:',student, ', Score:',score)

def getInforstudent():
    stu_id = input("Student ID: ")
    stu_name = input("Student name: ")
    stu_Dob = input("Student date of birth: ")
    stu = Student(stu_id, stu_name, stu_Dob)
    student.append(stu)
    return{"stu_id": stu_id,"stu_name": stu_name, "stu_Dob": stu_Dob }

def getCourse():
    cid = input("ID course: ")
    cname = input("Course name: ")
    lsco = Course(cid, cname)
    course.append(lsco)
    return{"cid": cid, "cname": cname}

def getScore():
    for c in course:
        for s in student:
            sc = input(f'Score of {s.get_sname()} in {c.get_cname()}: ')
            m = Score(c.get_cname(), s.get_sname(), sc)
            mark.append(m)

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
    for m in mark:
        m.mark()

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