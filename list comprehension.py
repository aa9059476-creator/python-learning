a=["python","code","codegnan"]
#["python","code","codegnan"]#print(a.upper())

'''b=str(a)
c=b.upper()
print(c)'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''#syntax
#a=[expression for var in collection/range)
a=[i.upper() for i in a]
print(a)'''

'''a=["vja","hyd","vza"]
#["vja","hyd","vza"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,2,3,4,5,6,8,12,13]
#b=[1,4,9,25,36,64,144,169]
c=[i**2 for i in a]
c=[i*i for i in a]
c=[pow(i,2) for i in a]
print(c)'''

#if usage in list comprehension
'''a=[i for i in range(21) if i%2==0]
print(a)'''

'''a=[i**2 for i in range(21) if i%2==0]
print(a)'''

fruits=["apple","banana","grapes","mango","kiwi","dragon","berry"]
'''b=[i for i in fruits if "a" in i]
print(b)'''

'''b=[i for i in fruits if "a"  in i]
print(b)'''

#no-elif usage in list comprehension
#if-else usage in list comprehension
'''a=[i**2 if i%2==0 else i*5 for i in range(31)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[i+j for i in a for j in b if i+j==6]
print(c)'''
