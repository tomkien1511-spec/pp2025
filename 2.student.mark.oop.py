class Student:
    def inputstudent(students):
        n = int(input("Number of students: "))
        for i in range(0, n, 1):
            sid = input("student id: ")
            sname = input("student name: ")
            dob = input("student dob: ")
            student = {"id": sid, "name": sname, "dob": dob}
            students.append(student)
    
    def __init__(self):
        self.students = []
        Student.inputstudent(self.students)

class Course:
    def inputcourse(courses):
        n = int(input("Number of courses: "))
        for i in range(0, n, 1):
            cid = input("course id: ")
            cname = input("course name: ")
            course = {"id": cid, "name": cname}
            courses.append(course)
    
    def __init__(self):
        self.courses = []
        Course.inputcourse(self.courses)

class Mark:
    def inputmark(marks, students, courses):
        for course in courses:
            print(f"Input marks for course {course["name"]}:")
            for student in students:
                markvalue = float(input(f"Mark for {student["name"]}: "))
                mark = {"sid": student["id"], "sname": student["name"], "cid": course["id"], "mark": markvalue}
                marks.append(mark)
    
    def __init__(self, students, courses):
        self.marks = []
        Mark.inputmark(self.marks, students, courses)  

def liststudents(students):
    print("List of Students:")
    for student in students:
        print(f"Id: {student["id"]}, Name: {student["name"]}, Dob: {student["dob"]}")

def listcourses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"Id: {course["id"]}, Name: {course["name"]}")

def listmarks(marks, courses):
    for course in courses:
        print(f"Marks for course {course["name"]}:")
        for mark in marks:
            if mark["cid"] == course["id"]:
                print(f"Student Id: {mark["sid"]}, Name: {mark["sname"]} Mark: {mark["mark"]}")

sobj = Student()
cobj = Course()
mobj = Mark(sobj.students, cobj.courses)
liststudents(sobj.students)
listcourses(cobj.courses)
listmarks(mobj.marks, cobj.courses)