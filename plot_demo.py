import numpy as np
import matplotlib.pyplot as plt

lin = np.linspace(2.0,3.0,num=5)
lin2 = np.linspace(2.0,3.0,num=5,endpoint=False)
lin3 = np.linspace(2.0,3.0,num=5,retstep=True)


N = 8
y = np.zeros(N*2)
x1 = np.linspace(0,10,N*2,endpoint=True)
x2 = np.linspace(0,10,N*2,endpoint=False)
plt.plot(x1,y,'x')
plt.plot(x2,y+0.5,'+')
plt.ylim([-0.3,1])
plt.show()

















