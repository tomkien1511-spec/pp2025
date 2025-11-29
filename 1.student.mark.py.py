students = []
courses = []
marks = {}
n = int(input("Number of students: "))
for i in range(0, n, 1):
    sid = input("student id: ")
    sname = input("student name: ")
    dob = input("student dob: ")
    student = {"id": sid, "name": sname, "dob": dob}
    students.append(student)
c = int(input("Number of courses: "))
for i in range(0, c, 1):
    cid = input("course id: ")
    cname = input("course name: ")
    course = {"id": cid, "name": cname}
    courses.append(course)
def givemark():
    cid = (input("course id for mark: "))
    for student in students:
        mark = (input(f"mark for {student["name"]}: "))
        if cid not in marks:
            marks[cid] = {}
        marks[cid][student["id"]] = float(mark)
givemark()        
print("List of student")
for student in students:
    print(f"Id: {student["id"]} Name: {student["name"]} Dob: {student["dob"]}")
print("List of course")
for course in courses:
    print(f"Id: {course["id"]} Name: {course["name"]}")
print("List of mark")
cname = (input("course name for mark: "))
print(f"Mark of {cname}: ")
for sid, mark in marks[cid].items():
    sname = next((s["name"] for s in students if s["id"] == sid), "Unknown")
    print(f"Student id: {sid}, Name: {sname}, Mark: {mark}")

