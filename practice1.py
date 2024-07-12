import pandas as pd
import numpy as np
a=[2,4,np.nan,6,7,np.nan]
b=pd.Series(a,index=['a','b','c','d','e','f'])
print(b.isnull())
df={
    'a':[2,5,4,np.nan,6],
    'b':[5,np.nan,np.nan,5,6],
    'c':[7,5,np.nan,4,2],
    'd':[9,2,4,5,6],
    'e':[5,2,np.nan,4,1]
}
df1=pd.DataFrame(df)
drop_na=df1.dropna()
print(drop_na.drop_duplicates())
b=['a','b','c','d','e']
c=['A','B','C','D','E']
d=pd.DataFrame(data=df,index=c,columns=b)
d['new']=d['a']+d['e']
print(d.loc[["A","B"]])
print(d.iloc[[0,4]])
print(d.reset_index(names=['amit']))
print(d.set_index('c'))
print(d.fillna(value=d.sum()))
print(d.sort_values(['a']))
print(d.value_counts('a'))
print(d.groupby('a').count())

# merge dataframe
data={
    "key": ["K0", "K1", "K2", "K3"],
    'a':[2,3,4,5],
    'b':[3,2,4,5]
}
data1={
    "key": ["K0", "K1", "K2", "K3"],
    'a':[5,3,4,5],
    'b':[9,2,4,5]
}
a=pd.DataFrame(data)
b=pd.DataFrame(data1)
# print(pd.concat([a,b],axis=1))
print(pd.merge(a,b,how='inner',on=['key']))
