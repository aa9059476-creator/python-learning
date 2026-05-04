Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic
>>> a=2
>>> b=4
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a//2)
1
>>> print(a/b)
0.5
>>> print(a**b)
16
>>> print(a%b)
2
>>> #assaignment
>>> a=3
>>> b=6
>>> print(a+b)
9
>>> print(a+b=)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> a+=b
>>> a
9
>>> a-=2
>>> a
7
>>> a*=4
>>> a
28
>>> a//=4
>>> a
7
>>> a/=2
>>> a
3.5
>>> a**=6
a
1838.265625
a%=4
a
2.265625
a
2.265625
b+=a
b
8.265625
b-=2
b
6.265625
b*=4
b
25.0625
b//=4
b
6.0
b/=2
b
3.0
b**=6
b
729.0
b%=4
b
1.0
a=5
b=9
#comparison
a=5
b=9
a<b
True
b>=a
True
a<=b
True
b>=a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a=6
b=6
a==b
True
#logical operators
a=6
b=3
a<b and b>a
False
a<b and b<a
False
a>b and b<a
True
a<=b and b>=a
False
a=5
b=9
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
#identify operators
a=5
if type(a) is int:
    print("true")

    
true
if type(a) is not int:
    print("its not int")

    
a=9
if type(a) is float:
    print("true")

    


if type(a) is not float:
    print("its not float")

    
its not float
#membership
a=4,5,6,7,8,9,10,11,12
if 10 in a:
    print(10)

    
10
if 15 in a:
    print(15)

    
if 15 not in a:
    print(15)

    
15
#bitwise
a=b
b=6
a&b
0
a=4
b=6
a&b
4
bin(4)
'0b100'
a&b
4
a=8
b=6
a^b
14
a=8
b=9
a^b
1
a=2
a<<2
8
a=4
a<<3
32
a=6
a<<4
96
a=5
a>>3
0
a=6
a>>2
1
