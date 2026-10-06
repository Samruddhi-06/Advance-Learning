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