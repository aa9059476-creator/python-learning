#annonymous functions(nameless functions)
#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("enter the value"))
b=lambda x:2*x+5
print(b(a))'''

'''a="codegnan"
a=lambda x: x.upper()
print(a("codegnan"))'''

'''a=input("data")
#codegnan
b=lambda a:a.upper()
print(b(a))'''

'''a="python course"
#python course"
b=lambda a:a.title()
print(b(a))'''

'''fname=input()
lname=input()
fullname=fname+lname
b=lambda b:fullname
print(b(fullname))'''

'''a,b=[x for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter()
#a=[5,8,9,10,20,40,37,87,67,59]
'''if a%2==0:
    print(a)'''#error

'''for i in a:
 if i%2==0:
     print(i)'''

'''b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),{},set()
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))'''

'''a=[[],(),set(),{}," ",None,6,7.8,"abbas",8+9j,True,False,"abdul"]
b=list(filter(None,a))
print(b)'''

#map()->each object from a collection and forms a new

'''a=[3,4,5,6,7,8,9,10,11]
b=[1,2,4,7,9,10,11,12]
c=list(map(max,a,b))
d=list(map(min,a,b))
e=list(map(sum,(a,b)))
print(c)
print(d)
print(e)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the values").split(",")
print(a+b)'''

'''a,b=[x for x in input("enter the names").split(",")
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=int(input("enter the values").split(",")
print(a+b)'''#error

'''a,b=[int(x) for x in input("enter the values").split(",")
print(a+b)'''

'''a,b=a,b=[int(x) for x in input("enter the values").split(",")
print(a+b)'''

'''a,b=list(map(int,input().split(",")))
print(a+b)'''

'''a,b=tuple(map(int,input().split(",")))
print(a+b)'''

'''a,b=set(map(int,input().split(",")))
print(a+b)'''

'''a=input("enter value")
b=dict(i.split(":") for i in a.split(","))
print(b)'''
    







