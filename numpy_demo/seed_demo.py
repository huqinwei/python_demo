import numpy as np

#default
##print(np.random.choice(5,3))
##print(np.random.randint(0,5,3))
##print(np.random.choice(5,3,p=[0.1, 0, 0.3, 0.6, 0]))
##print(np.random.choice(5,3,p=[0.1, 0, 0.1, 0.8, 0]))
##print('replace=False:',np.random.choice(5,3,replace=False))
##print('permutation:',np.random.permutation(np.arange(5))[:3])
##aa_milne_arr = ['pooh','rabbit','piglet','Christopher']
##print(np.random.choice(aa_milne_arr,5,p=[0.5, 0.1, 0.1, 0.3]))



#random.seed()
print('without seed')
print(np.random.choice(100,5))
print(np.random.choice(100,5))
print(np.random.choice(100,5))
print(np.random.choice(100,5))
np.random.seed(1)
print('seed(1)')
print(np.random.choice(100,5))
print(np.random.choice(100,5))
np.random.seed(1)
print(np.random.choice(100,5))
print(np.random.choice(100,5))

np.random.seed(2)
print('seed(2)')
print(np.random.choice(100,5))
print(np.random.choice(100,5))

np.random.seed(2)
print('seed(2)')
print(np.random.choice(100,5))
print(np.random.choice(100,5))


#to be continue
#di
#>>> help(np.random.RandomState)
#Examples
