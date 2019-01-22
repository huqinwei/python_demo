# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

from __future__ import print_function
import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,4,1]) # similar with 1D numpy
print(s)
dates = pd.date_range('20160101', periods=6)
dates2 = ['20160102','20160101','20160103','20140101','20160103','20160401',] 
df = pd.DataFrame(np.random.randn(6,4), index=dates2, columns=['A','B','C','D'])
print('df:\n',df)
print('df[B]:\n',df['B'])
df2 = pd.DataFrame({'A' : 1.,
                       'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                        'D' : np.array([3] * 4,dtype='int32'),
                        'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo'})
print(df2)
print(df2.dtypes)

print(df.index)
print(df.columns)
print(df.values)
#print(df.describe())
#print(df.T)
print('##############################')
print('index axis=0:\n',df.sort_index(axis=0, ascending=False))
print('index axis=0 ascending:\n',df.sort_index(axis=0, ascending=True))
print('index axis=1:\n',df.sort_index(axis=1, ascending=False))
print('index axis=1 ascending:\n',df.sort_index(axis=1, ascending=True))
#print(df.sort_index(axis=2, ascending=False))#no axis
#print(df.sort_values(by='B'))
df3 = pd.DataFrame({'A' : 1.,
                       'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                        'D' : np.array([3] * 4,dtype='int32'),
                        'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo'},columns=dates)
print('df3:\n',df3)
print(df3.dtypes)
