class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hi, my name is " + self.name)

p1 = Person("Alex", 21)
p1.greet()


class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hi, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our site.")

p1 = Person("Daniel")
p1.welcome()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Michael", 21)
print(p1.age)

p1.age = 22
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Alex", 28)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error


class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Daniel")
p2 = Person("Michael")

Person.lastname = "Smith"

print(p1.lastname)
print(p2.lastname)


class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("My Music")
my_playlist.add_song("Imagine")
my_playlist.add_song("Yesterday")
my_playlist.show_songs()
