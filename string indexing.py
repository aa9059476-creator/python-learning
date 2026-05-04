Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[4]
'y'
a[7]
'a'
a[0]
'v'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]=a[3]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[2]=a[3]
TypeError: 'str' object does not support item assignment
a=I love python
SyntaxError: invalid syntax
a="I love python"
a[2]+a[3]+a[4]+a[5]
'love'
a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'python'
a="vijayawada is a royal city"
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]
'is'
a="vizag is a city of destiny"
a="codegnan it solutions
SyntaxError: unterminated string literal (detected at line 1)
a="codegnan it solutions"
a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]a[-1]
SyntaxError: invalid syntax
a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'
a[-12]+a[-11]
'it'
a[-21]+a[20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'csdegnan'
#sicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work hard until you succeed
SyntaxError: unterminated string literal (detected at line 1)
a="work hard until you succeed"
a[:17]
'work hard until y'
a[17:]
'ou succeed'
a[:20]
'work hard until you '
a[20:]
'succeed'
a[10:]
'until you succeed'
a[10:16]
'until '
a[16:19]
'you'
a="i am learning python course"
a[2:4]
'am'
a[5:13]
'learning'
a[5:9]
'lear'
a[5:10]
'learn'
a[21:27]
'course'
a[14:20]
'python'
a="simple is better than complex"
a[-7:]
'complex'
a[-19:-13]
'better'
a[-29:-23]
'simple'
a="beautiful is better than ugly"
a[-29:20]
'beautiful is better '
a[-29:-20]
'beautiful'
a[-4;]
SyntaxError: invalid syntax
a[-4:]
'ugly'
a[-19:-17]
'is'
#striding
a="cloud computing
SyntaxError: unterminated string literal (detected at line 1)
a="cloud computing"
a[::5]
'c u'
a[:6]
'cloud '
a[8:]
'mputing'
>>> a[3:11]
'ud compu'
>>> a[::2]
'codcmuig'
>>> a[::7]
'cog'
>>> a[::1]
'cloud computing'
>>> a[5:12]
' comput'
>>> a="machine learning"
>>> a[2:11:3]
'cnl'
>>> a[3:15:4]
'h r'
>>> a[5:12:2]
'n er'
>>> a[1:10:5]
'ae'
>>> a="python course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2;-12:-4]
SyntaxError: invalid syntax
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-6]
'uh'
>>> a[-3:-9;-2]
SyntaxError: invalid syntax
>>> a[-3:-9:-2]
'ro '
>>> a="python course"
>>> a[7:4:2]
''
>>> a[-9:-5:-2]
''
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
