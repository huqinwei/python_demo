import numpy as np


scores = np.array([123,456,789])
scores2 = scores.copy()
print(scores)
scores -= np.max(scores)
print('scores:',scores)
print('scores2:',scores2)
p = np.exp(scores)/np.sum(np.exp(scores))
#p2 = np.exp(scores2)/np.sum(np.exp(scores2))
print('p:',p)
#print('p2:',p2)


print(np.exp(-1000))
print(np.exp(-100))
print(np.exp(-10))
print(np.exp(-1))
print(np.exp(0))
print(np.exp(1))
print(np.exp(10))
print(np.exp(100))
