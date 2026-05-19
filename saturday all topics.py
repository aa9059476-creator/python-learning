'''print("hello")
hello'''

'''a=input()
a
print(a)

a=['hello']
print(len(a))

for i in range(1,n):

a=4
print(type(a))'''



#dir()
#dir(""__builtins__"") we will get the built in functions printed

#max()

'''print(max(2,3,4,5,6,8,9,11,20,22,25))

#min
print(min(2,3,4,5,6,8,9,11,20,22,25))

#wrong method of sum
print(sum(2,5))

#sum
a=2,3,4,5,6
print(sum(a))'''

#from keys - converts single string into dictionary format
#fromkeys()
a="codegnan"
'''print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a)) - here we cant convert into dictionary directly

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"sam")
print(b)

#dict wont allow duplicate values so it will print n one time in codegnan

#here we can give the values to a certain key 
b["c"]="python"
print(b)'''

b=dict(zip(a))
print(b)

#evaluate - built in DataType, accepts all data types, for string use single '' or double ""

#eval()
'''while True:
    a=int(input("Enter"))
    b=int(input("enter"))
    print(a+b)'''

'''while True:
    a=float(input("Enter"))
    b=float(input("enter"))
    print(a+b)'''

'''while True:
    a=(input("Enter"))
    b=(input("enter"))
    print(a+b)'''

'''while True:
    a=eval(input("Enter"))
    b=eval(input("enter"))
    print(a+b)'''


#ZIP()

'''a=[10,20,30,40,50]
names=["sam","heart","bhaai","REed","tony"]
print(a+names)

# we shouldnt take zip() method directly , we need to assign data type
b=list(zip(a,names))
print(b)

b=tuple(zip(a,names))
print(b)

b=set(zip(a,names))
print(b)

b=dict(zip(a,names))
print(b)'''

#ENUMERATE -  WE CAN GIVE COUNTER TO THE COLLECTION

names= ["sam","heart","bhaai","REed","tony"]
'''for i in range(len(names)):
    print(i,names[i])'''

b=list(enumerate(names))
print(b)

b=list(enumerate(names,100))
print(b)

b=dict(enumerate(names))
print(b)

b=list(enumerate(names))
print(b)

#ASCII
#chr(),ord()
'''chr(56)
'8'
chr(90)
'Z'
chr(123)
'{'
ord("a")
97
ord("z")
122
'''
#here numbers should be assigned in chr  and alphabets in ord= ord("a")

'''for i in range(97,123):
    print(chr(i),end=" ")'''

'''for i in range(65,91):
    print(chr(i),end=" ")'''

a=input()
for i in a:
    print(i,ord(i))
