import numpy as np
import pandas as pd
rd=pd.read_csv("data1.csv")
print(rd.info())
df=pd.DataFrame(rd)
print(df.nunique())
print(rd.head())
print(rd.tail(7))

df['subtitute']=df['First Name']+df['Last Name']
print(df['subtitute'])
print(df.info())
print(df.info())
df.drop(columns=['City','Email'],axis=1)
print(df)
print(df.groupby('City').describe().transpose())
a=['a','a','a','b','b','b']
b=[1,2,3,1,2,3]
index=list(zip(a,b))
df=pd.MultiIndex.from_tuples(index)
d=pd.DataFrame(np.arange(12,24).reshape(6,2),df,columns=['A','M'])
print(d.sort_values('A',ascending=False))
print(d.pivot_table(values=None,index=['A','M'],columns='M',aggfunc=np.sum))
a={
    'a':[2,3,np.nan,np.nan],
    'b':[1,np.nan,6,4],
    'c':[5,np.nan,4,np.nan]
}
df=pd.DataFrame(a)
print(df)
print(df.dropna(thresh=2))
print(df['c'].isnull().sum())