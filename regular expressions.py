#regular expressions (regex)
'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\tin\nvja"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''\\w->it matches alphanumeric
\\w->it matches non-alpha-numeric
\\d->it matches any digits
\\D->it matches-non-digit
\\s->it represents white spaces
\\s->it represents non-white spaces'''

#compile()
import re
a="map maths cat cash money cup cap mug codegnan"
'''b=re.compile(r"m\w")
print(b)

#search()
c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#findall()
'''b=re.findall(r"m\w+",a)
print(b)'''

'''c=re.findall("c\w+",a)
print(c)'''

#split()
'''a=re.split(r"m",a)
print(a)'''

'''b=re.split(r"\S",a)
print(a)'''

#sub()
'''a=re.sub(r"maths","science",a)
print(a)'''

import re
'''a="year 2026 month 5 date 22"
b=re.findall(r"\d+",a)
print(b)'''

#syntax error
'''for i in range(10):
print(i)'''

#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''#10//0->zero division error

#logical error
'''a=4
b=9
if a<b:
    print("true")'''

#import mymodule

#exception handling
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")'''
        
    
    

