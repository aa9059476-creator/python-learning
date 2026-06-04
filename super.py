#sper()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=child("abbas",24)
print(a.name)
print(a.age)'''

#encapsulation
#publicdata()
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1.publicdata)
print(obj1.publicdata)'''

#_protecteddata()
'''class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()'''

#__privatedata()
'''class parent():
    __privatedata="abbas"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''


    
