import numpy

class Student:
    def __init__(self, students):
        self.students = students

class Course:
    def __init__(self, courses):
        self.courses = courses
        self.credits = numpy.array([c["credits"] for c in courses])

class Mark:
    def __init__(self, students, courses, marks, marks2):
        self.students = students
        self.courses = courses
        self.marks = marks
        self.marks2 = marks2
        self.credits = numpy.array([c["credits"] for c in courses])
        self.gpas = self.calallgpa()

    def calgpa(self, sindex):
        weightedsum = numpy.sum(self.marks[sindex] * self.credits)
        totalcredit = numpy.sum(self.credits)
        return weightedsum / totalcredit

    def calallgpa(self):
        return numpy.array([self.calgpa(i) for i in range(len(self.students))])

    def listgpa(self):
        sort = numpy.argsort(-self.gpas)
        print("GPA list:")
        for i in sort:
            print(f"Id: {self.students[i]['id']}, Name: {self.students[i]['name']}, GPA: {self.gpas[i]}")