Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#len()
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="code"
a[2]
'd'
a.find("d")
2
b="hello"
b.find("l")
2
b[2:4]
'll'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno\tmailid"
print(a)
name
mobileno	mailid
b="name:abbas\nmobileno:6301187720\tmailid:aa9059476@gmail.com
SyntaxError: unterminated string literal (detected at line 1)
b="name:abbas\nmobileno:6301187720\tmailid:aa9059476@gmail.com"
b
'name:abbas\nmobileno:6301187720\tmailid:aa9059476@gmail.com'
print(b)
name:abbas
mobileno:6301187720	mailid:aa9059476@gmail.com
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
#upper()
a="code"
a.upper()
'CODE'
#lower()
b="GNAN"
b.lower()
'gnan'
c="python"
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.capitalize()
'Python course'
e="i am in class"
e.title()
'I Am In Class'
a="data"
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isdigit()
False
b="python code"
b.isalpha()
False
c="pythoncoursese"
c.isalpha()
True
d="python_course"
d.isalpha()
False
a="abbas1234"
a.isdigit()
False
a="7.8"
a.isdecimal()
False
b=9.0
b.isdecimal()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    b.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
b="2"
b.isdecimal()
True
a="abbas"
b="abdul"
print(a+b)
abbasabdul
print(a+" "+b)
abbas abdul
print(a.title()+" "+b.title())
Abbas Abdul
print((a+" "+b).title())
Abbas Abdul
#strip()
#lstrip(),rstrip()
a="       abbas
SyntaxError: unterminated string literal (detected at line 1)
a=" abbas
SyntaxError: unterminated string literal (detected at line 1)
a="       abbas    "
a.strip()
'abbas'
a.lstrip()
'abbas    '
a.rstrip()
'       abbas'
#split()
a="python c c++ java"
a.split()
['python', 'c', 'c++', 'java']
b="iam learning python full stack"
b.split()
['iam', 'learning', 'python', 'full', 'stack']
a="apple","banana","mango"
"".join(a)
'applebananamango'
" ".join(a)
'apple banana mango'
"k".join(a)
'applekbananakmango'
#formating
a=5
b=9
print(a+b)
14
print("the sum is",a+b)
the sum is 14
print("the sum is,a+b")
the sum is,a+b
city="vja"
print("the city is",city)
the city is vja
#format method
a="motu"
>>> b="patlu"
>>> print("hello {}".format(a,b))
hello motu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> #fstring
>>> a="chota"
>>> b="bheem"
>>> print(f"hello {a}{b}")
hello chotabheem
>>> print(f"hello {a} {b}")
hello chota bheem
>>> print(f"hello {a} hello {b}")
hello chota hello bheem
>>> a=7
>>> b=8
>>> c=a*b
>>> print("multuiplication is".format(c))
multuiplication is
>>> print("multiplication is ()".format(c))
multiplication is ()
>>> print("multiplication is {}".format(c))
multiplication is 56
>>> print("multiplication is {}{}".format(c))
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    print("multiplication is {}{}".format(c))
IndexError: Replacement index 1 out of range for positional args tuple
>>> a=5
>>> b=3
>>> c=a*b
>>> print("the product is {}".format(c))
the product is 15
>>> print(f"the product is {c}")
the product is 15
>>> print("the product is {}".format(a*b))
the product is 15
>>> print(f"the product is {a*b}")
the product is 15
