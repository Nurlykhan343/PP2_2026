def my_function(fname):
  print(fname + " Smith")

my_function("Alex")
my_function("Daniel")
my_function("Michael")

def my_function(name): # name is a parameter
  print("Hi", name)

my_function("Alex") # "Alex" is an argument

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Alex", "Smith")

def my_function(country = "Canada"):
  print("I am from", country)

my_function("France")
my_function("Japan")
my_function()
my_function("Germany")


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "cat", name = "Milo")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("cat", "Milo")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("cat", name = "Milo", age = 3)

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["orange", "grape", "melon"]
my_function(my_fruits)
