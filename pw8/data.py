import pickle
import os
import gzip
import threading

def savedataasync(data):
    def _save():
        with gzip.open("students.dat", "wb") as f:
            pickle.dump(data, f)
    threading.Thread(target=_save, daemon=True).start()

def loaddata():
    if not os.path.exists("students.dat"):
        return None
    with gzip.open("students.dat", "rb") as f:
        return pickle.load(f)
    return data