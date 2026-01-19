import pickle
import os

def savedata(students, courses, marks, marks2):
    data = {"students": students, "courses": courses, "marks": marks, "marks2": marks2}
    with open("students.dat", "wb") as f:
        pickle.dump(data, f)

def loaddata():
    if not os.path.exists("students.dat"):
        return None
    with open("students.dat", "rb") as f:
        return pickle.load(f)