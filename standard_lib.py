# Python3 标准库概览
import os
print(os.getcwd())
# os.system('mkdir new_dir')
# os.chdir('/root')
# print(os.getcwd())


print(dir(os))
print(help(os))


import glob
print(glob.glob('*.py'))


import sys
print('sys.argv:',sys.argv)

# sys.stderr.write('Warning, log file not found starting a new one\n')

import re
print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1',r'\1','cat in the the hat'))
print('tea for too'.replace('too','two'))


import math
print(math.cos(math.pi / 4))
print(math.log(1024,2))
print(math.log(16,2))

import random
print(random.choice(['apple','orange','pear','banana']))
print(random.sample(range(100),10))
print(random.sample(range(80,100),10))
print(random.random())
print(random.random()*100  // 1)
print(int(random.random()*100))
print(random.randrange(6))


from datetime import date
now = date.today()
print(now)
yesterday = date(2008,12,12)
print(yesterday)
print(now.strftime('%m-%d-%y,%d %b %Y is a %A on the %d day of %B.'))

birthday = date(1987,11,2)
print(birthday)
age = now - birthday
print(age.days)
print(age)


#数据压缩

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(t)
de = zlib.decompress(t)
print(de)
print(len(de))
print(zlib.crc32(s))



#性能度量
from timeit import Timer
#好像就是算时间的，里边是语句，为什么分两个字符串，不清楚
#可能一句表达式是一个字符串,顺序是从右向左???不是，每一个参数不同，不是变参!!!!!!!!!!!
print(Timer('t=a;a=b;b=t','a=1;b=2').timeit())
print(Timer('a,b=b,a','a=1;b=2').timeit())
# print(Timer('a,b=b,a').timeit())UnboundLocalError: local variable 'b' referenced before assignment
# print(Timer('a=1;b=2','a,b=b,a').timeit())#UnboundLocalError: local variable 'b' referenced before assignment

# print(Timer('t = b','b=a','a=c','c = 5').timeit())    exec(code, global_ns, local_ns)           TypeError: exec() globals must be a dict, not str
# print(Timer('t=b','b=5','b=4').timeit())#TypeError: 'str' object is not callable
# print(Timer(code='t=b',global_ns='b=5',local_ns='b=4').timeit())TypeError: __init__() got an unexpected keyword argument 'global_ns'
# print(Timer(code='t=b',local_ns='b=4').timeit())TypeError: __init__() got an unexpected keyword argument 'local_ns'
# print(Timer(code='t=b').timeit())TypeError: __init__() got an unexpected keyword argument 'code'

##不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了不明白，先不管了



def average(values):
    return sum(values) / len(values)

import doctest
doctest.testmod()







# #处理get请求，不传data，则为get请求
#
# import urllib
# from urllib.request import urlopen
# from urllib.parse import urlencode
#
# url='http://www.baidu.com'
# data={"username":"admin","password":123456}
# req_data=urlencode(data)#将字典类型的请求数据转变为url编码
# res=urlopen(url+'?'+req_data)#通过urlopen方法访问拼接好的url
# res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
#
# print(res)
# #处理post请求,如果传了data，则为post请求
#
# import urllib
# from urllib.request import Request
# from urllib.parse import urlencode
#
# url='http://www.xxx.com/login'
# data={"username":"admin","password":123456}
# data=urlencode(data)#将字典类型的请求数据转变为url编码
# data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
# req_data=Request(url,data)#将url和请求数据处理为一个Request对象，供urlopen调用
# with urlopen(req_data) as res:
#     res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
#
# print(res)







