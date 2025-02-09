students = (
    ("Rana", 20, 85),
    ("Riyad", 22, 78),
    ("Rony", 21, 92),
    ("Emtiaz", 23, 88),
    ("Mishal", 19, 76)
)
sorted_students = sorted(students, key=lambda student: student[2])
print("Students sorted:")
for student in sorted_students:
    print(student)
