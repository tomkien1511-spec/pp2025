import zipfile
import os

datafiles = ["students.txt", "courses.txt", "marks.txt"]
archive = "students.dat"

def compressdata():
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in datafiles:
            if os.path.exists(file):
                zf.write(file)

def decompressdata():
    if not os.path.exists(archive):
        return False
    with zipfile.ZipFile(archive, "r") as zf:
        zf.extractall()
    return True
