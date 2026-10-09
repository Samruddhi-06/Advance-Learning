import pandas as pd

# Series using read_csv

subs = pd.read_csv('Pandas/Pandas_Series/subs.csv').squeeze()
print(subs)
print(type(subs))
print()

# Series with 2 cols

vk = pd.read_csv('Pandas/Pandas_Series/kohli_ipl.csv', index_col='match_no').squeeze()
print(vk)
print()  

bwood = pd.read_csv('Pandas/Pandas_Series/bollywood.csv', index_col='movie').squeeze()
print(bwood)
print(type(bwood))
print()

# Series methods

# head and tail
print("Heads")
print(vk.head())
print(vk.head(10))
print()

print("tails")
print(subs.tail())
print(subs.tail(10))
print()

# sample
print("Random movie samples")
print(bwood.sample())
print(bwood.sample(5))
print()

# value_counts
print(bwood.value_counts())
print()

# sort_values
print(vk.sort_values())
print(vk.sort_values(ascending=False))
print(vk.sort_values(ascending=False).head(3).values[0])
print()

# sort_index
print(bwood.sort_index())
print()

