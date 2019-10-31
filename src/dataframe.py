import pandas as pd


df=pd.read_csv('/home/abzooba/PycharmProjects/ReyazTest/data/demofile.csv')
# print(df)

print(df.info())
print(df)

res=df.dtypes
#print(res)
print('--------------------------------')

df['Id']=df['Id'].astype(int)
# Here the column Id is changed to integer type
print(df.info())
print(df)

print('--------------------------------')

df['Activate'] = df['Activate'] =='Y'
'''
   In a dataframe we can filter a data based on a column value in order to filter data, we can apply 
   certain condition on dataframe. When we apply these operator on dataframe then it produce a Series of 
   True and False.
   Here in Activate Column we are checking for Y, it will result in True rest will be in false.
'''
print(type(df))

#df["Activate"]=df["Activate"].str.replace('Y','True')
#df["Activate"]=df["Activate"].str.replace('N','False')
#df.loc[df.Activate == 'Y','Activate']='True'
#df.loc[df.Activate == 'N','Activate']='False'

print(df)
#print(df.info())

print('********************************')
df['2016'] = df['2016'].str.replace(r'\D', '').astype(int)
df['2017'] = df['2017'].str.replace(r'\D', '').astype(int)

''' 
Here r represents raw string, Any value other than integer get replaced by 2nd argument i.e. blank ('') 
In raw string it may be character/special character either in start/end/middle it will replaced by 2nd argument
here blank ('')       
'''

print(df)
print(df.info())

c=df['2016']+df['2017']
print(c)


