# Python3 模块
#str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。



s = "Hello, World"
print(str(s))
print(repr(s))


#有些区别用这个print显示不出来，因为已经被print给转换了,得用终端交互，直接输入表达式来打印，就有区别了
#感觉repr就是一种给机器的格式，str就是人为调整的固定形式。但是print也支持了很多格式控制，str.format
# str.format()
print((1/7))
print(str(1/7))


# >>> for x in range(1, 11):
# ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
# ...     # 注意前一行 'end' 的使用
# ...     print(repr(x*x*x).rjust(4))
# ...

# >>> for x in range(1, 11):
# ...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# ...

# >>> 'l2'.zfill(5)
# '000l2'
# >>> '-3.15'.zfil(7)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'zfil'
# >>> '-3.15'.zfill(7)
# '-003.15'
# >>> '3.1412431231'.zfill(5)
# '3.1412431231'
#
#
#
# #原来花括号就能传参了，不用里边的数字，数字主要可以调整、颠倒顺序
# >>> str1 = '{0},,,,,{1},'.format(33,55)
# >>> str1
# '33,,,,,55,'
# >>> str2 = '{}....{}'.format(44,55)
# >>> str2
# '44....55'
# >>> str3 = '{1},,,{0}'.format(33,55)
# >>> str3
# '55,,,33'
# >>> str4 =
#   File "<stdin>", line 1
#     str4 =
#           ^
# SyntaxError: invalid syntax
# >>> str4 = '{name}....{age}'.format(33,44)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'name'
# >>> str4 = '{name}....{age}'.format(name = 'hu',age = 44)
# >>> str4
# 'hu....44'
# >>> str4 = '{age}....{age}'.format(name = 'hu',age = 44)
# >>> str4
# '44....44'
# >>> str4 = '{age}....{name}'.format(name = 'hu',age = 44)
# >>> str4
# '44....hu'
# >>> str5 = '{0},{1},{name}'.format(name = 'hu',100,1000)
#   File "<stdin>", line 1
# SyntaxError: positional argument follows keyword argument
# >>> str5 = '{0},{1},{name}'.format(10,100,name = 'hu',100,1000)
#   File "<stdin>", line 1
# SyntaxError: positional argument follows keyword argument
# >>> str5 = '{0},{1},{name}'.format(10,100,name = 'hu')
# >>> str5
# '10,100,hu'
# >>> str5 = '{0},{1},{name}'.format(name = 'hu',100,1000)
#   File "<stdin>", line 1
# SyntaxError: positional argument follows keyword argument
# >>> str5 = '{0},{1},{name}'.format(name = 'hu',100)
#   File "<stdin>", line 1
# SyntaxError: positional argument follows keyword argument
# >>> str5 = '{0},{1},{name}'.format(name = 'hu',100)

#虽然关键字和纯下标可以自由结合，但是感觉限制挺多的




#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:



# >>> import math
# >>> print('PI similar to:{}'.format(math.pi))
# PI similar to:3.141592653589793
# >>> print('PI similar to:{!r}'.format(math.pi))
# PI similar to:3.141592653589793
# >>> 'PI similar to:{!r}'.format(math.pi)
# 'PI similar to:3.141592653589793'
# >>> 'PI similar to:{}'.format(math.pi)
# 'PI similar to:3.141592653589793'
# >>> print('pi similar to {0:.3f}'.format(math.pi))
# pi similar to 3.142
# >>> print('pi similar to {5:.3f}'.format(math.pi))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: tuple index out of range
# >>> print('pi similar to {0:.3f}'.format(math.pi))
# pi similar to 3.142
# >>> print('pi similar to {1:.3f}'.format(math.pi))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: tuple index out of range
# >>> print('pi similar to {0:.3f}'.format(math.pi))
# pi similar to 3.142
# >>> print('pi similar to {2:.3f}'.format(math.pi,8888.9999))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: tuple index out of range
# >>> print('pi similar to {1:.3f}'.format(math.pi,8888.9999))
# pi similar to 8889.000
# >>> print('pi similar to {1:3.3f}'.format(math.pi,8888.9999))
# pi similar to 8889.000
# >>> print('pi similar to {1:5.3f}'.format(math.pi,8888.9999))
# pi similar to 8889.000
# >>> print('pi similar to {1:5.5f}'.format(math.pi,8888.9999))
# pi similar to 8888.99990
# >>> table = {'google':1,'baidu':2,'taobao':3}
# >>> for name,number in table.items():
# ...     print('{0:10} ==> {1:10d}'.format(name,number))
# ...
# baidu      ==>          2
# taobao     ==>          3
# google     ==>          1
# >>> print('ali:{0['Taobao']:d}; g:{0['google']:d};  b:{0['baidu']:d}'.format(table))
#   File "<stdin>", line 1
#     print('ali:{0['Taobao']:d}; g:{0['google']:d};  b:{0['baidu']:d}'.format(table))
#                         ^
# SyntaxError: invalid syntax
# >>> print("ali:{0['Taobao']:d}; g:{0['google']:d};  b:{0['baidu']:d}".format(table))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: "'Taobao'"
# >>> print("ali:{0[Taobao]:d}; g:{0[google]:d};  b:{0[baidu]:d}".format(table))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Taobao'
# >>> table
# {'baidu': 2, 'taobao': 3, 'google': 1}
# >>> print("ali:{0[taobao]:d}; g:{0[google]:d};  b:{0[baidu]:d}".format(table))
# ali:3; g:1;  b:2
# >>> print("ali:{0['taobao']:d}; g:{0[google]:d};  b:{0[baidu]:d}".format(table))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: "'taobao'"
# >>> print("ali:{0[taobao]:d}; g:{0[google]:d};  b:{0[baidu]:d}".format(table))
# ali:3; g:1;  b:2
#下标还可以这样用，format只跟一个table，然后用下标去table取值，不过这个下标key不用加引号
#也可以通过在 table 变量前使用 '**' 来实现相同的功能：
# >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# >>> print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
# Runoob: 2; Google: 1; Taobao: 3


#旧式字符串格式化
# >>> print('pi : %5.3f'%math.pi)
# pi : 3.142





>>> f = open('this_is_a_file','w')
>>> f.write('hello file')
10
>>> f.close()
>>> f = open('this_is_a_file','r')
>>> print(f)
<_io.TextIOWrapper name='this_is_a_file' mode='r' encoding='UTF-8'>
>>> f.read()
'hello file'
>>> f.read(4)
''
>>> f.read(5)
''
>>> f.close()
>>> f = open('this_is_a_file','r')
>>> f.read(3)
'hel'
>>> f.read(3)
'lo '
>>> f.read(3)
'fil'
>>> f.read(3)
'e'
>>>


f.readline()


f.readlines()


如果要写入一些不是字符串的东西, 那么将需要先进行转换:

#!/usr/bin/python3

# 打开一个文件
f = open("/tmp/foo1.txt", "w")

value = ('www.runoob.com', 14)
s = str(value)
f.write(s)

# 关闭打开的文件
f.close()
执行以上程序，打开 foo1.txt 文件：

$ cat /tmp/foo1.txt
('www.runoob.com', 14)














































