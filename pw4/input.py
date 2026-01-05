import numpy
import math

def decimalfloor(n):
    return math.floor(n * 10) / 10

def inputstudents():
    students = []
    n = int(input("Number of students: "))
    for i in range(0, n, 1):
        sid = input("student id: ")
        sname = input("student name: ")
        dob = input("student dob: ")
        student = {"id": sid, "name": sname, "dob": dob}
        students.append(student)
    return students

def inputcourses():
    courses = []
    n = int(input("Number of courses: "))
    for i in range(0, n, 1):
        cid = input("course id: ")
        cname = input("course name: ")
        credit = int(input("course credits: "))
        course = {"id": cid, "name": cname, "credits": credit}
        courses.append(course)
    return courses

def inputmarks(students, courses):
    marks2 = []
    ns = len(students)
    nc = len(courses)
    marks = numpy.zeros((ns, nc))
    for j, course in enumerate(courses):
        print(f"\nInput marks for course {course['name']}:")
        for i, student in enumerate(students):
            value = float(input(f"Mark for {student['name']}: "))
            marks[i, j] = decimalfloor(value)
            mark = {"sid": student["id"], "sname": student["name"], "cid": course["id"], "mark": marks[i, j]}
            marks2.append(mark)
    return marks, marks2