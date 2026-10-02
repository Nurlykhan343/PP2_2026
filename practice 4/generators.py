#iter and next examples
#1
mytuple = ("orange", "grape", "melon")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

#2
mystr = "orange"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#3
mytuple = ("orange", "grape", "melon")
for x in mytuple:
  print(x)

#4
mystr = "orange"
for x in mystr:
  print(x)

#5
class MyNumbers:
  def __iter__(self):
    self.a = 5
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#6
class MyNumbers:
  def __iter__(self):
    self.a = 5
    return self

  def __next__(self):
    if self.a <= 15:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#generators
#1
def my_generator():
  yield 5
  yield 6
  yield 7

for value in my_generator():
  print(value)

#2
def count_up_to(n):
  count = 2
  while count <= n:
    yield count
    count += 1

for num in count_up_to(6):
  print(num)

#3
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(500000)
print(next(gen))
print(next(gen))
print(next(gen))

#4
def simple_gen():
  yield "Alex"
  yield "David"
  yield "Mark"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#5
# List comprehension - creates a list
list_comp = [x * x for x in range(6)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(6))
print(gen_exp)
print(list(gen_exp))

#6
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(8))
print(total)

#7
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 50 Fibonacci numbers
gen = fibonacci()
for _ in range(50):
  print(next(gen))

#8
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hi")
gen.send("Bye")

#9
def my_gen():
  try:
    yield 4
    yield 5
    yield 6
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
