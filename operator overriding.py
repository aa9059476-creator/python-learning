#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(4)
#x=5
#y=4
print(x+y)'''

#method overloading
''''class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("thee product is",a*b)
        else:
            print("program ends.....")
a=New()
a.sum
a.sum(3,4,5)
a.sum(6,4)'''

'''class New():
    def sum(self, *values):
        if len(values) == 3:
            a, b, c = values
            print("the sum is", a + b + c)

        elif len(values) == 2:
            a, b = values
            print("the product is", a * b)

        else:
            print("program ends.....")

a= New()
a.sum()
a.sum(3, 4, 5)
a.sum(6, 4)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dong can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

# Method Overriding

'''class Vehicle():
    def move(self):
        print("Vehicle can move")

class Car(Vehicle):
    def move(self):
        print("Car runs on roads")

a = Vehicle()
b = Car()

a.move()
b.move()'''
