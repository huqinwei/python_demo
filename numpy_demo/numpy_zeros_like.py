
import numpy as np

x = np.arange(6).reshape(2,3)
x2 = np.arange(3, dtype = float)
print(x)
y = np.zeros_like(x)
print(y)
y2 = np.zeros_like(x2)
print(y2)


