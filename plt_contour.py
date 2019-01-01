import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    Z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
    return Z

n=256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

X,Y = np.meshgrid(x,y)
plt.contourf(X, Y, f(X,Y),12, alpha=0.75, cmap=plt.cm.hot)
C = plt.contour(X,Y,f(X,Y), colors = 'black', linewidth=5)
plt.clabel(C, inline = False, fontsize = 20)


plt.xticks(())
plt.yticks(())

plt.show()







