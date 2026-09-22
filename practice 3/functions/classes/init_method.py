class Person:
  pass

p1 = Person()
p1.name = "Alex"
p1.age = 21

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age=20):
    self.name = name
    self.age = age

p1 = Person("Daniel")
p2 = Person("Michael", 22)

print(p1.name, p1.age)
print(p2.name, p2.age)
