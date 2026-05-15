#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[5,6,7,8,9,10]
check(*b)
c={8,9,10,11,12}
check(*c)
d={"name":"abbas","city":"vja"}
check(*d)'''

'''def check1(*a):
    b=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i)==int or type(i) ==float:
            b=b+i
            print(b)
    
check1()
check1(2,3,4,5,6,7)
check1(1,2,3,4,5.2,4.3)
check1(2,3,5,7,2.4,5.3,"abbas")'''

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30],
   "names":["abbas","abdul","pandu"],
   "status":["P","A","P"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"idnos":[10,20,30],
   "names":["abbas","abdul","pandu"],
   "status":["P","A","P"]}
details(**d)'''

#both * and **usage
'''def final(*a,**b):
    d=1#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,4.6,3.2,"python",7+9j,True,False)
final(*data)
details={"idnos":[10,20,30],
    "names":["abbas","abdul","pandu"],
    "status":["P","A","P"]}
final(**details)
final(*data,**details)'''


