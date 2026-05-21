Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#math
import math
math.pi
3.141592653589793
math.pi*3
9.42477796076938
math.sqrt(2)
1.4142135623730951
math.tan(45)
1.6197751905438615
>>> math.cos(60)
-0.9524129804151563
>>> math.pow(2,4)
16.0
>>> math.sin(30)
-0.9880316240928618
>>> math.log(20)
2.995732273553991
>>> math.ceil(3.9)
4
>>> math.ceil(4.4)
5
>>> math.ceil(5,9)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    math.ceil(5,9)
TypeError: math.ceil() takes exactly one argument (2 given)
>>> math.lcm(2,22)
22
>>> math.lcm(2,2)
2
>>> math.hcf(20,2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    math.hcf(20,2)
AttributeError: module 'math' has no attribute 'hcf'
>>> math.lcm(2,25)
50
>>> math.floor(5,9)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    math.floor(5,9)
TypeError: math.floor() takes exactly one argument (2 given)
>>> math.floor(5)
5
>>> math.floor(5.6)
5

SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers




'''import mymodule
mymodule.greetings("dhanush")'''

'''import mymodule
a=mymodule.details["idnos"]
b=mymodule.details["names"]
c=mymodule.details["marks"]
print(a)
print(b)
print(c)'''

#import mymodule
SyntaxError: multiple statements found while compiling a single statement

'''def greetings(name):
    print("welcome",name)'''

'''a=10
b=20
print("the sum is",a+b)'''


'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''


'''details={"idnos":[10,20,30],
         "names":["sam","ram","dead"],
...          "marks":[50,60,70]}'''
... 
... if __name__=="__main__":
...     a=[10,20,30,40,50]
...     a.append("code")
...     #a.extend("code")
...     print(a)
... 
... 
... def dummy():
...     if __name__=="__main__":
...         print("the program is run as script")
...     else:
...         print("this program is run as module")
... dummy()
... 
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> #Difference btw module , library, package
... #Module-
... ''' a module in python is a single python file it consists python code.
... it typically consists of functions,classes,variables,that can be used in other pythom scripts or programs
... examples of modules inclide mac.py,random.py,my_module.py'''
... 
... 
... #package
... '''a package in python is a directy containing one or more python modules and an __init__.py file
... the __init__.py file can be empty or contains initialization code for the package
... examples of packages include numpy,pandas or django'''
... 
... 
... #Library
... '''library can consist of multiple modules and packages, organized to serve a particular purpose or domain
... examples of library such as requests,numpy,pandas,matplotlib'''
... 
... #NOte
... '''every python file is a module and import is a keyword , every python file is saved internally with variable name as __main__'''
