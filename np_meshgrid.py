import numpy as np
import matplotlib.pyplot as plt

nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
print('nx:', nx)
print('ny:', ny)
print('x:', x)
print('y:', y)
print('xv:', xv)
print('xv\'s shape', xv.shape)
print('yv:', yv)

xv, yv = np.meshgrid(x, y, sparse = True)
print('xv:', xv)
print('xv\'s shape', xv.shape)
print('yv:', yv)
print('yv\'s shape', yv.shape)

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
print('xx:', xx)
print('xx\'s shape', xx.shape)
print('yy:', yy)
print('yy\'s shape', yy.shape)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
# z = np.sin(xx**2 + yy**2)
# z = xx**2 + yy**2
# z = xx + yy
h = plt.contourf(x,y,z)
plt.show()

    # `meshgrid` is very useful to evaluate functions on a grid.
    #
    # >>> x = np.arange(-5, 5, 0.1)
    # >>> y = np.arange(-5, 5, 0.1)
    # >>> xx, yy = np.meshgrid(x, y, sparse=True)
    # >>> z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
    # >>> h = plt.contourf(x,y,z)