# Pandas Series

# Series from lists

import numpy as np
import pandas as pd

# String

country = ['India', 'China', 'SriLanka', 'Nepal', 'Japan']
print(pd.Series(country))

# integer

runs = [56,12,0,15,55,100]
print(pd.Series(runs))

# custom index

marks = [57,66,89,98]
subjects = ['Science', 'english', 'hindi', 'maths']

print(pd.Series(marks,index=subjects))

# setting a name

print(pd.Series(marks,index=subjects, name='Marks of roll no. 21'))

# series from dictionary

marks = {
    'Chemistry' : 87,
    'Physics' : 96,
    'Biology' : 90,
    'Maths' : 97
}
print(pd.Series(marks, name='marks of samruddhi'))


# Serirs attributes

marks_series = pd.Series(marks, name='Marks of student 1')

# size
print(marks_series.size)

# dtype
print(marks_series.dtype)

# name
print(marks_series.name)

# is_unique
print(marks_series.is_unique)

# index
print(marks_series.index)

# values
print(marks_series.values)