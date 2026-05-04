Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[4,6.7, "python",5+9j,True,False]
print(a)
[4, 6.7, 'python', (5+9j), True, False]
type(a)
<class 'list'>
c=[8.9]
type(c)
<class 'list'>
a.append("html")
a
[4, 6.7, 'python', (5+9j), True, False, 'html']
a.append("java,"guvi")
         
SyntaxError: unterminated string literal (detected at line 1)
a.append("java","guvi")
         
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append("java","guvi")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["css","java"])
         
a
         
[4, 6.7, 'python', (5+9j), True, False, 'html', ['css', 'java']]
#extend()
         
a=["ds","ai","ml"]
         
a.extend(["abbas","gupta","loki","snehit"])
         
a
         
['ds', 'ai', 'ml', 'abbas', 'gupta', 'loki', 'snehit']
a.insert(0,"1st pos changed")
         
a
         
['1st pos changed', 'ds', 'ai', 'ml', 'abbas', 'gupta', 'loki', 'snehit']
#sort()
         
a=["white","black","red","pink"]
         
a.sort()
         
a
         
['black', 'pink', 'red', 'white']
b=[7,9,4,0,2,5,711]
         
b.sort()
         
b
         
[0, 2, 4, 5, 7, 9, 711]
b=["@","#","&","!","*"]
         
b.sort()
         
b
         
['!', '#', '&', '*', '@']
#reverse()
         
a=["hi","hello","how"]
         
a.reverse()
         
a
         
['how', 'hello', 'hi']
b=[7,8,9,10,11,50]
         
b.reverse()
         
b
         
[50, 11, 10, 9, 8, 7]
a=[2,3,4,5,6]
         
a.sort()
         
a
         
[2, 3, 4, 5, 6]
#pop()
         
a=[3,4,5,7,10]
         
a.pop()
         
10
a
         
[3, 4, 5, 7]
a.pop(4)
         
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.pop(4)
IndexError: pop index out of range
a.pop (4)
         
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.pop (4)
IndexError: pop index out of range
a.pop(4)
         
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.pop(4)
IndexError: pop index out of range
a.pop(3)
         
7
a
         
[3, 4, 5]
#remove()
         
a.remove(4)
         
a
         
[3, 5]
a=[3,6,8,10,20,30]
         
len(a)
         
6
a="hello"
         
len(a)
         
5
b=["hello"]
         
len(b)
         
1
b=["python","java","c"]
         
b.count('c")
        
SyntaxError: unterminated string literal (detected at line 1)
b.count("c")
        
1
#tuple()
        
a=(5,6,7,8,9,10)
        
print(a)
        
(5, 6, 7, 8, 9, 10)
type(a)
        
<class 'tuple'>
b=(3,7.8,"python",4+9j,True,False)
        
type(b)
        
<class 'tuple'>
len(a)
        
6
a.index(10)
        
5
b.count(4+9j)
        
1
c=[5,6,7,8,9,10]
        
c=(4,5,6,7,8,9)
        
c.count(10)
        
0
c.count(8)
        
1
a=[9,1,5,2,8,4,6,3,7,0]
        
#[7,6,4,3,0,9,8,5,2,1]
        
len(a)
        
10
b=a[:5]
        
>>> a1
...         
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a1
NameError: name 'a1' is not defined. Did you mean: 'a'?
>>> a1=a[:5]
...         
>>> a1
...         
[9, 1, 5, 2, 8]
>>> a2=a[5:10]
...         
>>> a2
...         
[4, 6, 3, 7, 0]
>>> a1.sort()
...         
>>> a1
...         
[1, 2, 5, 8, 9]
>>> a2.sort()
...         
>>> a2
...         
[0, 3, 4, 6, 7]
>>> a1.reverse()
...         
>>> a1
...         
[9, 8, 5, 2, 1]
>>> a2.reverse()
...         
>>> a2
...         
[7, 6, 4, 3, 0]
>>> c=a2+a1
...         
>>> c
...         
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
