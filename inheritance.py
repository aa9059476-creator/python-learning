#single inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        #print("avaible cash is",cls.cash)
        print("avaible cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        #print("new_cash is",cls.cash+cls.cash)
        print("new_cash is",cls.cash+RBI.cash)
a=HDFC()
print(dir(a))
a.available_cash()
a.new_cash()'''

#multiple inheritance
'''class Father():   # Parent Class 1
    height = 6
    def show_height(cls):
        print("Father height is", Father.height)
class Mother():   # Parent Class 2
    weight = 55
    def show_weight(cls):
        print("Mother weight is", Mother.weight)
class Kid(Father, Mother):   # Child Class
    dob = "10-05-2010"
    def show_dob(cls):
        print("Kid DOB is", Kid.dob)
a = Kid()
print(dir(a))
a.show_height()
a.show_weight()
a.show_dob()'''

#multilevel inheritance
'''class GrandParent():# Parent Class 1
    land = 10
    def show_land(cls):
        print("GrandParent land is", GrandParent.land)
class Parent(GrandParent):# Parent Class 2
    house = 2
    def show_house(cls):
        print("Parent house is", Parent.house)
class Child(Parent):# Child Class
    vehicle = 1
    def show_vehicle(cls):
        print("Child vehicle is", Child.vehicle)
a = Child()
print(dir(a))
a.show_land()
a.show_house()
a.show_vehicle()'''

#hierarchical
'''class Employee():# Parent Class
    company = "Codegnan"
    def show_company(cls):
        print("Company name is", Employee.company)
class Trainer(Employee):# Child Class 1
    subject = "Python"
    def show_subject(cls):
        print("Trainer teaches", Trainer.subject)
class Developer(Employee):# Child Class 2
    language = "Java"
    def show_language(cls):
        print("Developer works with", Developer.language)
b = Developer()
print(dir(b))
b.show_company()
b.show_language()'''

#hybrid
class College:
    college_name = "SVH College"
    def show_college(self):
        print("College Name:", College.college_name)
class Student(College):
    student_name = "Abbas"
    def show_student(self):
        print("Student Name:", Student.student_name)
class Sports:
    sport = "Cricket"
    def show_sport(self):
        print("Sport:", Sports.sport)
class Result(Student, Sports):
    grade = "A"
    def show_grade(self):
        print("Grade:", Result.grade)
a = Result()
print(dir(a))
a.show_college()
a.show_student()
a.show_sport()
a.show_grade()
