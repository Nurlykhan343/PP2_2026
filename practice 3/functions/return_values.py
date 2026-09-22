def my_function(x, y):
  return x + y

result = my_function(7, 4)
print(result)

def my_function():
  return ["orange", "grape", "melon"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function(x, y):
  return x + y

result = my_function(7, 4)
print(result)

def my_function():
  return (15, 25)

x, y = my_function()
print("x:", x)
print("y:", y)


def my_function(name, /): # positional only
  print("Hi", name)

my_function("Alex")

def my_function(*, name): # keyword only
  print("Hi", name)

my_function(name = "Alex")

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(7, 12, c = 18, d = 23)
print(result)
