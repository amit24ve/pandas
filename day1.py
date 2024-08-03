# import pandas as pa
# data ={
#     "a":[1,4,5,7],
#     "d":['a','s','e','t']
# }
# # f=pa.Series(index=['usa','tokyo','china','india','up'],data=[2,4,5,6,7])
# f=pa.DataFrame(data)
# g=pa.Series(data)
# print(f) 
# print(g)

# # print(pa.random.seed(100))
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)

# import pandas as pd
# import numpy as np
# c=pd.read_csv("data.csv")
# print(c.tail(5))
# print(c.head(5))
# print(c.info())
# print(c.drop_duplicates(inplace=True))
# print(c.describe())
# c=np.random.rand(6,6)
# print(pd.DataFrame(c,['a','b','c','d','e','f'],['A','B','C','D','E','F']))

import pandas as pd
import numpy as np
data={
    'a':[1,2,np.nan],
    'b':[5,np.nan,np.nan],
    'c':[2,3,4]
}
# df=pd.DataFrame(a,['5','6','7'],['a','b','c'])
# print(df.dropna(thresh=2))
# print(df.fillna(value=3))
# print(df)
# df=pd.DataFrame(a)
# print(df.fillna(value=df['b'].count()))
# print(df)
# df=pd.DataFrame(data)
# df['new']=df['a']+df['b']
# print(df.drop('new',axis=1))
df=pd.DataFrame(data,['5','6','7'],['a','b','c'])
print(df.loc[['a','b']])# import pandas as pa
# data ={
#     "a":[1,4,5,7],
#     "d":['a','s','e','t']
# }
# # f=pa.Series(index=['usa','tokyo','china','india','up'],data=[2,4,5,6,7])
# f=pa.DataFrame(data)
# g=pa.Series(data)
# print(f)
# print(g)

# # print(pa.random.seed(100))
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)

# import pandas as pd
# import numpy as np
# c=pd.read_csv("data.csv")
# print(c.tail(5))
# print(c.head(5))
# print(c.info())
# print(c.drop_duplicates(inplace=True))
# print(c.describe())
# c=np.random.rand(6,6)
# print(pd.DataFrame(c,['a','b','c','d','e','f'],['A','B','C','D','E','F']))

import pandas as pd
import numpy as np
data={
    'a':[1,2,np.nan],
    'b':[5,np.nan,np.nan],
    'c':[2,3,4]
}
# df=pd.DataFrame(a,['5','6','7'],['a','b','c'])
# print(df.dropna(thresh=2))
# print(df.fillna(value=3))
# print(df)
# df=pd.DataFrame(a)
# print(df.fillna(value=df['b'].count()))
# print(df)
# df=pd.DataFrame(data)
# df['new']=df['a']+df['b']
# print(df.drop('new',axis=1))
df=pd.DataFrame(data,['5','6','7'],['a','b','c'])
print(df.loc[['a','b']])# import pandas as pa
# data ={
#     "a":[1,4,5,7],
#     "d":['a','s','e','t']
# }
# # f=pa.Series(index=['usa','tokyo','china','india','up'],data=[2,4,5,6,7])
# f=pa.DataFrame(data)
# g=pa.Series(data)
# print(f)
# print(g)

# # print(pa.random.seed(100))
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)

# import pandas as pd
# import numpy as np
# c=pd.read_csv("data.csv")
# print(c.tail(5))
# print(c.head(5))
# print(c.info())
# print(c.drop_duplicates(inplace=True))
# print(c.describe())
# c=np.random.rand(6,6)
# print(pd.DataFrame(c,['a','b','c','d','e','f'],['A','B','C','D','E','F']))

# import pandas as pd
# import numpy as np
# data={
#     'a':[1,2,np.nan],
#     'b':[5,np.nan,np.nan],
#     'c':[2,3,4]
# }
# df=pd.DataFrame(a,['5','6','7'],['a','b','c'])
# print(df.dropna(thresh=2))
# print(df.fillna(value=3))
# print(df)
# df=pd.DataFrame(a)
# print(df.fillna(value=df['b'].count()))
# print(df)
# df=pd.DataFrame(data)
# print(df)
# df['new']=df['a']+df['b']
# print(df.drop('new',axis=1))
# df=pd.DataFrame(data,['5','6','7'],['a','b','c'])
# print(df.loc[['a','b']])

# a="amit".split()
# print(a)

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={"id":"student_id","first":"first_name","last":"last_name","age":"age_in_years"},inplace=True)
    return students
