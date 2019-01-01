import sys
print(sys.path)
#python
#python -m

root@ubuntu:/home/qw/Documents/python_test# python3 python_m.py
['/home/qw/Documents/python_test', '/usr/local/lib/python3.5/dist-packages/setuptools-19.6-py3.5.egg', '/home/qw/Documents/python_test', '/home/qw/Documents/python_test/slim', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']

root@ubuntu:/home/qw/Documents/python_test# python3 -m python_m.py
['', '/usr/local/lib/python3.5/dist-packages/setuptools-19.6-py3.5.egg', '/home/qw/Documents/python_test', '/home/qw/Documents/python_test/slim', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']
/usr/bin/python3: Error while finding spec for 'python_m.py' (AttributeError: module 'python_m' has no attribute '__path__')

