# Here is multiple inheritance
class Student:
    def study(self):
        print("Student is learning")


class Athlete:
    def train(self):
        print("Athlete is exercising")


class SportsStudent(Student, Athlete):
    pass


person = SportsStudent()
person.study()
person.train()
