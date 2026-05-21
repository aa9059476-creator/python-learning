#GENERATORS
'''NO TUPLE COMPREHENSION IN ABOVE CASES IF WE REMOVE THOSE BRACES
AND KEEP PARANTHESIS AND OUTCOME IS GENERATOR'''

#a=[expr for var in collection/range]
'''a=[i for i in range(21)]
print(a)
print(type(a))'''


'''a=(i for i in range(21))
print(*a)#here we use *argument
print(type(a))'''


'''a=(i for i in range(21))
print(list(a))#here no need of *argument, we given datatype
print(type(a))'''

'''a=(i for i in range(21))
print(tuple(a))
print(type(a))'''

'''a=(i for i in range(21))
print(set(a))
print(type(a))'''

'''a=(i for i in range(21))
print(dict(a))#we cannot pass dictionary in generator types
print(type(a))'''


###A GENERATOR IS ALSO A FUNCTION WHICH CAN BE USED AS AN ITERATOR(LOOP) BY PRODUCING GROUP OF VALUES,WHERE WE USE YIELD KEYWORD.

#YIELD VS RETURN
'''RETURN WILL TERMINATE THE FUNCTION WHERE AS
YIELD CAN PASS THE FUNCTION AND GO ON WITH EVERY SUCCESSIVE ITERATION'''


'''a,b=[int(x) for x in input("enter the values").split(",")] # here this method is used insted of map for 2input functions
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''


'''a,b=[int(x) for x in input("enter the values").split(",")] # here this method is used insted of map for 2input functions
def check(a,b):
    while a<b:

        yield a
        a=a+1
        #yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")] # here this method is used insted of map for 2input functions
def check(a,b):
    while a<b:
        a=a+1
        return a # no need to use * argument for return
print(check(a,b))'''


#yield v/s return
'''def mygen():
    #return "python"
    #return "Java"
    #return "DSA"
    return "java","python","dsa"
print(*mygen())'''


'''def mygen():
    yield "vja"
    yield "vzg"
    yield "hyd"
print(*mygen())

#NEXT()-
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
'''

#GLOBAL AND LOCAL VAriableS

#VARIABLES INSIDE AND OUTSIDE THE FUNCTION IS CALLED GLOBAL AND LOCAL VARIABLES

# A VARIABLE DEFINE ABOVE THE FUNCTION AND IS ACCESSABLE TO THE ENTIRE GLOBAL SPACE IS CALLED GLOBAL VARIABLE

#A VARIABLE DEFINE INSIDE THE FUNCTION IS CALLED LOCAL VARIABLE

 #GLOBAL VARIABLE FIRST CASE
'''a=3
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)
'''

'''a=2
def check1():
    a=5
    a=a**2
    print("inside value",a)
check1()
print("outside values",a)'''


#third case of both global and local variables
'''a=4
b=6
def check2():
    a=5
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b values is",b)'''

#USAGE OF GLOBAL 
'''USAGE OF GLOBAL KEYWORD-WHEN USER WANTS TO ACCESS THE GLOBAL VARIABLE INSIDE THE FUNCTION DIRECTLY AND
CARRY FORWARD THE UPDATED VALUE EVEN OUTSIDE THE FUNCTION
THEN WE USE GLOBAL KEYWORD'''

'''a=4
def check2():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    #global b
    b=12# local variable
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b values is",b)'''











        
        
        
