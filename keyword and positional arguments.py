#keyword and positional arguments

'''def details(id,name,mailid):
    id=10
    name="abbas"
    mailid="abbas@codegnan.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="abbas",mailid=a@gmail.com)
Details(id=30,name="akash",mailid=a@gmail.com)
Details(40,"jagadeesh","j@gmail.com")
Details("pandu","p@gmail.com",50)
Details(mailid="a@gmail.com",id=60,name="abbas")'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("sugar",100)'''

'''def grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="ghee",price):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(500)'''

#cake,price,qty
def cake(cake_name, price, quantity):
    print("Cake name is %s" % cake_name)
    print("Price is %.2f" % price)
    print("Quantity is %d" % quantity)
cake("Chocolate Cake", 500, 2)

#* argument->* is used to unpack the elements
'''a=[2,3,4,5,6,7]
print(a)
print(*a)
print(type(a))'''

'''a=[2,3,4,5,6,7]
print(a)
print(*a)
print(type(a))'''

'''a={2,3,4,5,6,7}
print(a)
print(*a)
print(type(a))'''

'''a={"year":2026,"month":5}
print(a)
print(*a)
print(type(a))'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4,5,6,7,8,9,10,11,12,13
print(*a)
print(b)
print(c)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''
























