# Arbitrary Arguments - *args-tuple
def my_function(*students):
  print("The youngest student is " + students[2])

my_function("Alex", "Daniel", "Michael")

# args becomes a tuple containing all the passed arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hi", "Alex", "Daniel", "Michael")

# **kwargs-dictionary

def my_function(**person):
  print("His last name is " + person["lname"])

my_function(fname = "Daniel", lname = "Smith")

def my_function(**mydata):
  print("Type:", type(mydata))
  print("Name:", mydata["name"])
  print("Age:", mydata["age"])
  print("All data:", mydata)

my_function(name = "Daniel", age = 21, city = "Almaty")

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("Student Info", "Alex", "Daniel", age = 21, city = "Astana")
