import numpy as np
import pandas as pd
ra=np.random.rand(5,5)
df=pd.DataFrame(ra,['A', 'B', 'C', 'D', 'E'],["a","b","c","d","e"])
df['new']=df['a']+df['b']
print(df)
print(df.drop('new',axis=1))
print(df.loc[['A','B']])
print(df.iloc[[0,1,2,3]])
a=['a','b','c','a','b','c']
b=[1,1,1,2,2,2]
c=list(zip(b,a))
ind=pd.MultiIndex.from_tuples(c)
d=np.random.random((6,2))
df=pd.DataFrame(d,ind,['A','B'])
print(df.xs(1,axis=0))
print(df.loc[2].loc['a']['A'])

df=pd.DataFrame(ra,['A', 'B', 'C', 'D', 'E'],["a","b","c","d","e"])
a=np.array([[2,3,4],[5,6,6]])
b=np.array([[5,7,5],[5,6,6]])
c=np.array([[6,4,3],[9,8,6]])
df1=pd.DataFrame(a)
print(df1.scatter_matrix())
df2=pd.DataFrame(b)
df3=pd.DataFrame(c)
print(pd.concat([df1,df2,df3,df1],axis=1))
print(pd.merge(df1,df2,how='inner'))
print(df1.join(df2))
print(df1[1].unique())
def times(s):
    return s*2
print(df1[0].apply(times))
print(df1.pivot_table(values=1,index=[0,1],columns=[0,1]))