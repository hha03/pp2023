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
    print(f'Enter marks for students in {c["cname"]} :')
    for s in student:
        score = float(input(f'{s["stu_name"]} :'))
        s.setdefault("score",{})[c['cid']] = score

n = int(input("Number of students: "))
student = []
for i in range(n):
    print('Student ' + str(i+1) +':')
    s = getInforstudent()
    student.append(s)
    
k = int(input("Number of course: "))
course = []
for i in range(k):
    print('Course ' + str(i+1) +':')
    c = getCourse()
    course.append(c)

for c in course:
    getScore()


for s in student:
        print(f'ID: {s["stu_id"]},  Name: {s["stu_name"]},  Date of Birth: {s["stu_Dob"]}')
        for c in course:
            print(f'    ID Course: {c["cid"]}, Course: {c["cname"]}, Score: {s["score"][c["cid"]]}')