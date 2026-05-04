Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets{}
>>> a={2,6.7,"python",7+9j,True,False}
>>> print(a)
{False, True, 2, (7+9j), 'python', 6.7}
>>> type(a)
<class 'set'>
>>> #add()
>>> a={2,3,4,5,6}
>>> a.add(10)
>>> a
{2, 3, 4, 5, 6, 10}
>>> a={1,2,3,4,5,6}
>>> b={4,5,6}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> a={6,7,8,9,10,11,12}
>>> b={9,10,11,12}
>>> a.issuperset(b)
True
>>> b.issubset(a)
True
>>> #union()
>>> a={1,2,3,4,5,6,7}
>>> b={5,6,7,8,9,10,11}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> #intersection
>>> a={4,5,6,7,8,9}
>>> b={6,7,8,9,10}
>>> a.intersection(b)
{8, 9, 6, 7}
>>> #update()
>>> a={3,4,5,6,7,8}
>>> b={5,6,7,8,9,10}
>>> a.update(b)
>>> a
{3, 4, 5, 6, 7, 8, 9, 10}
a
{3, 4, 5, 6, 7, 8, 9, 10}
b
{5, 6, 7, 8, 9, 10}
b.update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10}
b
{3, 4, 5, 6, 7, 8, 9, 10}
#difference()
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.difference(b)
{3, 4, 5}
b.difference(a)
{10, 11}
#symmentric_difference
a={2,3,4,5,6,7}
b={1,5,6,7,8,9,10}
a.symmentric_difference(b)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.symmentric_difference(b)
AttributeError: 'set' object has no attribute 'symmentric_difference'. Did you mean: 'symmetric_difference'?
a.symmentricdifference(b)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.symmentricdifference(b)
AttributeError: 'set' object has no attribute 'symmentricdifference'. Did you mean: 'symmetric_difference'?
a.symmentric_difference(b)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.symmentric_difference(b)
AttributeError: 'set' object has no attribute 'symmentric_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)
{1, 2, 3, 4, 8, 9, 10}
a={4,5,6,7,8,9,10}
b={7,8,9,10,11,12}
a.difference_update(b)
a
{4, 5, 6}
a
{4, 5, 6}
b.difference_update(a)
b
{7, 8, 9, 10, 11, 12}
#symmetric_difference_update
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.symmetric_diffrence_update(b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.symmetric_diffrence_update(b)
AttributeError: 'set' object has no attribute 'symmetric_diffrence_update'. Did you mean: 'symmetric_difference_update'?
a.symmetric_difference_update(b)
a
{1, 2, 7, 8}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8}
#clear()
a={3,4,5,6,7,8,9,10}
b={9,10,11,12,13,14}
a.copy()
{3, 4, 5, 6, 7, 8, 9, 10}
a.clear()
a
set()
b=set()
b.add(10,20,30)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    b.add(10,20,30)
TypeError: set.add() takes exactly one argument (3 given)
b.add(20)
b
{20}
a={10,20,30,40,50}
a.pop()
50
a.pop(30)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.pop(30)
TypeError: set.pop() takes no arguments (1 given)
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.remove(30)
a
{20, 40, 10}
#discard
a={100,200,300,400}
b={300,400,500,600}
a.discard(100)
a
{300, 400, 200}
a.isdisjoint(b)
False
#dict{}
a={"year":2026, "month":5}
print(a)
{'year': 2026, 'month': 5}
type(a)
<class 'dict'>
b={"year", "month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['year', 'month'])
a.values()
dict_values([2026, 5])
a.items()
dict_items([('year', 2026), ('month', 5)])
a={"name":"abbas","mailid":"aa9059476@gmail.com"}
a.update({"mobileno":6301187720})
a
{'name': 'abbas', 'mailid': 'aa9059476@gmail.com', 'mobileno': 6301187720}
a.update({"year":2026,"month":5})
a
{'name': 'abbas', 'mailid': 'aa9059476@gmail.com', 'mobileno': 6301187720, 'year': 2026, 'month': 5}
#set default
a={"year":2026,"month":"may"}
a.setdefault("date",2)
2
a
{'year': 2026, 'month': 'may', 'date': 2}
#pop()
a={"year":2026,"month":"may"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("year")
2026
a
{'month': 'may'}
a.popitem()
('month', 'may')
a
{}
a={"time":1,"min":3,"sec":4}
a.copy()
{'time': 1, 'min': 3, 'sec': 4}
a["time"]
1
a.get("min")
3
a
{'time': 1, 'min': 3, 'sec': 4}
a={"name":"abbas","city":"vij"}
a.clear()
a
{}
b={}
b.update({"course":"python"})
b
{'course': 'python'}
details={"idnos":[10,20,30],"names":["vara","ravali","appu"],"marks":[70,80,90]}
type(details)
<class 'dict'>
a.keys()
dict_keys([])
details.keys()
dict_keys(['idnos', 'names', 'marks'])
details.values()
dict_values([[10, 20, 30], ['vara', 'ravali', 'appu'], [70, 80, 90]])
details.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['vara', 'ravali', 'appu']), ('marks', [70, 80, 90])])
