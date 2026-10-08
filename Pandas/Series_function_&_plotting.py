import pandas as pd
import matplotlib.pyplot as plt

# Series Indexing

x = pd.Series([12,56,86,0,32,11])

print(x[4])

print(x[2:5])

# fancy indexing
vk: pd.Series = pd.read_csv('Pandas/kohli_ipl.csv', index_col='match_no').squeeze()

print(vk[[1,3,8]])

# indexing with label
bwood = pd.read_csv('Pandas/bollywood.csv', index_col='movie').squeeze()
print(bwood['Why Cheat India'])

# Editing series

# using indexing 

marks = {
    'Chemistry' : 87,
    'Physics' : 96,
    'Biology' : 90,
    'Maths' : 97
}
marks_series = pd.Series(marks, name='Marks of student 1')

marks_series[1] = 100
print(marks_series)

# what if index does not exists

marks_series['Marathi'] = 75
print(marks_series)

# slicing
# can edit multiple items

marks_series[1:3] = [55,45]
print(marks_series)

# fancy indexing

x[[0,3,4]] = [0,0,0]
print(x)

# series with python functionalities
print(len(bwood))
print(type(vk))
print(dir(vk))
print(sorted(bwood))
print(max(vk))
print(min(vk))

# type conversion

print(list(vk))
print(list(bwood))

# membership operator

print('Abhay Deol' in bwood.values)

# looping
for i in bwood:
    print(i)
for i in bwood.index:
    print(i)

# Boolean Indexing in series

print(vk[vk >= 50])
print(vk[vk >= 50].size)

print(vk[vk == 0])
print(vk[vk == 0].size)

num = bwood.value_counts()
print(num[num > 20])

# plotting graphs in series

vk.plot()
plt.show()

bwood.value_counts().head(20).plot(kind='bar')
plt.show()
bwood.value_counts().head(20).plot(kind='pie')
plt.show()