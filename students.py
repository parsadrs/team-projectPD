# students.py
students = []

def sort_students(by="Firstname"):
    if by == "Firstname":
        return sorted(students, key=lambda s: s['Firstname'])
    elif by == "LastName":
        return sorted(students, key=lambda s: s['LastName'])
    elif by == "SID":
        return sorted(students, key=lambda s: s['SID'])
    else:
        return students
