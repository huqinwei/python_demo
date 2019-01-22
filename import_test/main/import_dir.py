import import_func
import_func.func_print(a=12,b=1)
# from . import import_func
#python3:SystemError: Parent module '' not loaded, cannot perform relative import
#python2:ValueError: Attempted relative import in non-package



import sys

sys.path.append("/home/qw/Documents/python_test/import_test/lib")
print(sys.path)

import import_func2
import_func2.func_print(a=11,b=1)

