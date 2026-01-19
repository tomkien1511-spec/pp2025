import numpy
import math

def decimalfloor(n):
    return math.floor(n * 10) / 10

def inputstudents():
    students = []
    n = int(input("Number of students: "))
    with open("students.txt", "a") as f:
        for i in range(0, n, 1):
            sid = input("student id: ")
            sname = input("student name: ")
            dob = input("student dob: ")
            student = {"id": sid, "name": sname, "dob": dob}
            students.append(student)
            f.write(f"{sid},{sname},{dob}\n")
    return students

def inputcourses():
    courses = []
    n = int(input("Number of courses: "))
    with open("courses.txt", "a") as f:
        for i in range(0, n, 1):
            cid = input("course id: ")
            cname = input("course name: ")
            credit = int(input("course credits: "))
            course = {"id": cid, "name": cname, "credits": credit}
            courses.append(course)
            f.write(f"{cid},{cname},{credit}\n")
    return courses

def inputmarks(students, courses):
    marks2 = []
    ns = len(students)
    nc = len(courses)
    marks = numpy.zeros((ns, nc))
    with open("marks.txt", "a") as f:
        for j, course in enumerate(courses):
            print(f"\nInput marks for course {course['name']}:")
            for i, student in enumerate(students):
                value = float(input(f"Mark for {student['name']}: "))
                marks[i, j] = decimalfloor(value)
                mark = {"sid": student["id"], "sname": student["name"], "cid": course["id"], "mark": marks[i, j]}
                marks2.append(mark)
                f.write(f"{student['id']},{student['name']},{course['id']},{marks[i, j]}\n")
    return marks, marks2