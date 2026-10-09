import pandas as pd
import numpy as np

# Some important Series methods

# astype

vk = pd.read_csv('Pandas/Pandas_Series/kohli_ipl.csv', index_col='match_no').squeeze()

print(vk.astype('int16'))

# between

print(vk[vk.between(49,69)])
print(vk[vk.between(49,69)].size)

# clip

subs = pd.read_csv('Pandas/Pandas_Series/subs.csv').squeeze()
print(subs.clip(100,200))

# drop_duplicates

temp = pd.Series([0,0,1,np.nan,2,3,2,3,1,4,5,5])
print(temp)
print(temp.drop_duplicates())
print(temp.drop_duplicates(keep='last'))
print(temp.duplicated())
print(temp.duplicated().sum())

# isnull

print(temp.isnull())
print(temp.isnull().sum())

# dropna

print(temp.dropna())

# fillna

print(temp.fillna(temp.mean()))

# isin

print(vk[vk.isin([49,99])])

# apply


print(vk.apply(lambda x: 'good day' if x > vk.mean() else 'bad day'))

# copy

new = vk.head().copy()
new[1] = 100
print(new)
print(vk)