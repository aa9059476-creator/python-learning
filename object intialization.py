#object intialization
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("abbas",24,"vja")
print(dir(a))
a.display()'''

'''class Details():
    # creating a constructor
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Place:", self.place)

# runtime input
name = input("Enter name: ")
age = int(input("Enter age: "))
place = input("Enter place: ")

# creating object
a = Details(name, age, place)

print(dir(a))

# calling method
a.display()'''

#diff b/w _ and __
'''class Employee():
    def __init__(self):
        self.name="abbas"
        self.__salary=10000#private variable
        self._mailid="aa9059476@gmail.com"
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee__salary)'''

'''class Employee1:
    def __init__(self,name,mail,salary):
        self.name=name
        self._mail=mail
        self.__salary=salary
    def display(self):
        print(self.name,self._mail,self.__salary)
e1=Employee1('abbas','aa9059476@gmail.com',30000)
class Employee2:
    def __init__(self,name,mail,salary):
        self.name=name
        self._mail=mail
        self.__salary=salary
    def display(self):
        print(self.name,self._mail,self.__salary)
e2=Employee2('abbas','aa9059476@gmail.com',31000)
e1.display()
e2.display()'''

#polymorphism

#operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(10))
print(a.__sub__(1))
print(a.__mul__(6))
#print(a.__div__(2))
print(a.__pow__(2))
print(a.__ge__(10))
print(a.__le__(20))
a=[1,2,3,4,5,6];b=[5,6,7,8,9,10,11]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="python";b="course"
print(a.__add__(b))
a="code";b="gnan"
print(a.__add__(b))
print("abbas".__add__("abdul"))
a="abbas";b="abdul"
print((a.__add__(" "+b)).title())'''

