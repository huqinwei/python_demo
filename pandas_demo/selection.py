import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
df2 = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','C','T','TT'])
print('df:\n',df)
#print("df.A:\n",df.A)
#print("df['A']:\n",df['A'])
#print("df[0:3]:\n",df[0:3])
#print("df['2013-01-02':'2013-01-04']:\n",df['2013-01-02':'2013-01-04'])
#print("df['2013-01-02','2013-01-04']:\n",df['2013-01-02','2013-01-04'])



#print("df2.A:\n",df2.A)
#print("df2.B:\n",df2.B)
#print("df2.C:\n",df2.C)
#print("df2.T:\n",df2.T)
#print("df2.TT:\n",df2.TT)


#loc
print("###################")
#print(df.loc['20130102'])
#print(df.loc[:,['A','B']])#otherwise?how to do the same thing?
#print(df.loc[['A','B']])#error:not in index!!!!!!!
#print(df.loc['20130102',['A','B']])


#iloc
print(df.iloc[3])
print(df.iloc[3][1])
#print(df.iloc[[2:4,0:2]])#more [] error
print(df.iloc[2:4,0:2])
#print(df.iloc[[2,3,4,0:2]])
#print(df.iloc[2:4],[0:2])#less [] error
#print(df.iloc[[2,3,4],[0:2]])#: not allowed
print(df.iloc[[2,3,4],[0,2]])
#ix
print(df.ix[:3,['A','C']])
#boolean
print(df[df.A > 0])







