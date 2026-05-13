#functions
#without function
'''
a=10
b=20
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
'''
#using function block
'''
def calculate(a,b):
    print("the sum is",a+b)
    print("the difference is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)
'''
'''
def calculate(a,b):
    print("the power is",a**b)
    print("the modulus is",a%b)
    print("the division is",a/b)
calculate(4,5)
calculate(25,5)
calculate(1000,5)
'''
#runtime
'''
def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
add()
'''

'''
def fullname():
    fname=input("first name ")
    lname=input("last name ")
    print((fname+" "+lname).title())
fullname()

'''
'''
def data():
    print("python")
data()
'''

#print v/s return

'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)
'''
'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e #only in this case, all values are printed.
print(cal(2,4))
 '''
#my method which is wrong
'''
def calc(a,b):

    c=int(input())
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
        return()        
calc(2,3)    
'''
#correct method
'''
def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(enter the option
                                         1.add
                                         2.sub
                                         3.mul))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
    else:
        print("invalid option")
cal()
 '''   

'''
#2nd method
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("value of a "))
    b=int(input("value of b "))
    option=int(input(enter the option
                                         1.add
                                         2.sub
                                         3.mul))
    if option == 1:
        add()
    elif option == 2:
        sub()
    elif option == 3:
        mul()
    else:
        print("invalid")
'''

#split
'''
def cal():
    a=int(input("total amount "))
    b=int(input("total members "))


    print("per head ",a/b)
cal()

'''

'''
def cal():
    a=int(input("total amount "))
    b=int(input("total members "))
    c=a/b


    print(f"per head {c}",)
cal()
'''
'''
def cal():
    a=int(input("total amount "))
    b=int(input("total members "))
    c=a/b
    
    print("per head {}".format(c))  
    
cal()                                        
'''

#madam method
'''
while True:
    def splitbill():
    
        a=int(input("total amount "))
        b=int(input("total members "))
        print("per head is ",a//b)
    splitbill()
    
'''

        
    
    











    
