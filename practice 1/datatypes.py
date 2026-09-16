x = 15
y = 4.25
z = "hello"

print(type(x))
print(type(y))
print(type(z))


name = "Aruzhan"
age = 19
gpa = 3.5
is_student = True

print(name, type(name))
print(age, type(age))
print(gpa, type(gpa))
print(is_student, type(is_student))


countries = ["Japan", "Turkey", "Germany"]
visited = {"Kazakhstan", "Turkey"}

print(countries, type(countries))
print(visited, type(visited))


age = "19"
print(age, type(age))

age = int(age)
print(age, type(age))

next_year = age + 1
print("Next year I will be", next_year)


numbers = range(2, 12)

print("Numbers:", list(numbers))
print("Data type:", type(numbers))
