from input import inputstudents, inputcourses, inputmarks
from domains import Student, Course, Mark
from data import savedataasync, loaddata

open("students.txt", "w").close()
open("courses.txt", "w").close()
open("marks.txt", "w").close()

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
def main():
    data = loaddata()
    if data is None:
        studentsdata = inputstudents()
        coursesdata = inputcourses()
        marksarray, markslist = inputmarks(studentsdata, coursesdata)
    else:
        studentsdata = data["students"]
        coursesdata = data["courses"]
        marksarray = data["marks"]
        markslist = data["marks2"]
    sobj = Student(studentsdata)
    cobj = Course(coursesdata)  
    mobj = Mark(studentsdata, coursesdata, marksarray, markslist)
    liststudents(sobj.students)
    listcourses(cobj.courses)
    listmarks(mobj.marks2, cobj.courses)
    mobj.listgpa()
    savedataasync({"students": studentsdata,"courses": coursesdata, "marks": marksarray, "marks2": markslist})

if __name__ == "__main__":
    main()