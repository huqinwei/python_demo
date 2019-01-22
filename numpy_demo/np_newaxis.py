import numpy as np

# numeric.py
# newaxis = None

a = np.array([1,2,3])
print(a)
print(a[:,np.newaxis])
print(a[:,None])
print(None == np.newaxis)





