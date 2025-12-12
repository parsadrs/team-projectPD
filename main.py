# main.py
from students import students, sort_students
from add_students import students as dev_students

# اضافه کردن اطلاعات developers به آرایه اصلی
students.extend(dev_students)

print("Sorted by Firstname:")
print(sort_students("Firstname"))

print("Sorted by LastName:")
print(sort_students("LastName"))

print("Sorted by SID:")
print(sort_students("SID"))