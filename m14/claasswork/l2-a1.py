import pandas as pd
import numpy as np

mydataset = {
    'cars' : ['BMW', 'Mercedes', 'Tesla'],
    'passings': [3,7,4]
    }

df1 = pd.DataFrame(mydataset)
print(df1)
df = pd.DataFrame(mydataset, index=[1,2,3])
print(df)

print(df.iloc[0,0])  #position or index
print(df.loc[1,['cars']])  #label 

#series
a = [1,2,3]
ser1 = pd.Series(a)
print(ser1)
ser = pd.Series([1,2,3], index=['a','b','c'])
print(ser)
ser2 = pd.Series({"day1": 520, "day2": 390, "day3":230})
print(ser2)


#Load files
df = pd.read_csv("Countries Data.csv")
print(df.head())
print(df.info())
print("is null:", df.isnull().sum())
#df_new = df.dropna()   #inplace = True
#print(df_new)

#df = pd.read_csv("Countries Data.csv")
#print(df.fillna(130, inplace=True))