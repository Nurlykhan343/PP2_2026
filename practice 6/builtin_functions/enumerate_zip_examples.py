students = ["Tom", "Kate", "John"]
years = [17, 18, 19]

print("Enumerate:")
for number, student in enumerate(students):
    print(number, student)

print("Zip:")
for student, year in zip(students, years):
    print(student, year)