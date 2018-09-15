import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
print(s)
print(type(s))

dates = pd.date_range('20180101',periods=5)
print(dates)

dates = pd.date_range('20180101',freq='M',periods=6)
print(dates)


df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df)


df = pd.DataFrame({'A':1.,
		'B':pd.Timestamp('20130102'),
		'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		'D':np.array([3]*4,dtype='int32'),
		'E':pd.Categorical(["test","train","test","train"]),
		'F':'foo'})
print(df)
print(df.dtypes)
print('index:',df.index)
print('columns:',df.columns)
#print(df.rows)
print(df.values)
print(df.describe())
print(df.T)
print(df.sort_index(axis=0))
print(df.sort_index(axis=1))
print(df.sort_index(axis=1,ascending=False))
print(df.sort_index(axis=0,ascending=False))
print(df.sort_values(by='E'))
#print(df.sort_values(by=2))


