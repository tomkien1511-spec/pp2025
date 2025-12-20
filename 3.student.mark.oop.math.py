import math
import numpy

def decimalfloor(n):
    return math.floor(n * 10) / 10

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
            credit = int(input("course credits: "))
            course = {"id": cid, "name": cname, "credits": credit}
            courses.append(course)

    def __init__(self): 
        self.courses = []
        Course.inputcourse(self.courses)

class Mark:
    def __init__(self, students, courses):
        self.mark2 = []
        self.students = students
        self.courses = courses
        ns = len(students)
        nc = len(courses)
        self.marks = numpy.zeros((ns, nc))
        for j, course in enumerate(courses):
            print(f"Input marks for course {course['name']}:")
            for i, student in enumerate(students):
                markvalue = float(input(f"Mark for {student['name']}: "))
                self.marks[i, j] = decimalfloor(markvalue)
                mark = {"sid": student["id"], "sname": student["name"], "cid": course["id"], "mark": markvalue}
                self.mark2.append(mark)
        self.gpas = self.calallgpa()

    def calgpa(self, sindex):
        weightedsum = numpy.sum(self.marks[sindex] * self.ccredit())
        totalcredit = numpy.sum(self.ccredit())
        return weightedsum / totalcredit
    
    def ccredit(self):
        return numpy.array([c["credits"] for c in self.courses])
    
    def calallgpa(self):
        return numpy.array([self.calgpa(i) for i in range(len(self.students))])
    
    def listgpa(self):
        sort = numpy.argsort(-self.gpas)
        print("GPA list:")
        for i in sort:
            print(f"Id: {self.students[i]['id']}, Name: {self.students[i]['name']}, GPA: {self.gpas[i]}")

def liststudents(students):
    print("List of Students:")
    for student in students:
        print(f"Id: {student["id"]}, Name: {student["name"]}, Dob: {student["dob"]}")

def listcourses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"Id: {course["id"]}, Name: {course["name"]}")

def listmarks(marks2, courses):
    for course in courses:
        print(f"Marks for course {course["name"]}:")
        for mark in marks2:
            if mark["cid"] == course["id"]:
                print(f"Student Id: {mark["sid"]}, Name: {mark["sname"]} Mark: {mark["mark"]}")

sobj = Student()
cobj = Course()
mobj = Mark(sobj.students, cobj.courses)
liststudents(sobj.students)
listcourses(cobj.courses)
listmarks(mobj.mark2, cobj.courses)
mobj.listgpa()