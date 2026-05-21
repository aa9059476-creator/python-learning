#random module
'''import random
a=random.sample(range(10,40),10)
print(a)'''

#randint()
'''import random
a=random.randint(30,50)
print(a)'''

#choice()
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

#dice code
#import random
'''n = input("enter the roll of Dice")
a = random.randint(1, 6)
print("Dice value =", a)
while True:
    input("enter the roll of dice")
    a=random.randit(1,6)
    print(a)
    option=input("roll again? y/n")
    if option=='y':
        continue
    elif option=="n":
        break
    else:
        print("invalied option")'''

#calendar
'''import calendar
year=2026
month=5
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

#task
'''import calendar
n=int(input())
m=int(input())
print(calendar.month(n,m))'''

#date& time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

import time
'''a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")'''

import random
import time

'''for i in range(10):
    num = random.randint(1, 10)
    print(num)
    time.sleep(2)'''


