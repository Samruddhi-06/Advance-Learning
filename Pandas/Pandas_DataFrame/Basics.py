# importing pandas and numpy

import pandas as pd
import numpy as np

# Creating DataFrame

# using lists -> 2D list required

student_data = [
    [100, 80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
students = pd.DataFrame(student_data, columns=['iq','marks','package'])
print(students)
print()

# using dictionary

student_dict = {
    'name' : ['Ram','Shyam','Kiran', 'Mohan'],
    'iq': [100,90,120,80],
    'marks': [80,70,100,50],
    'package': [10,7,14,2]
}

student = pd.DataFrame(student_dict)
student.set_index('name', inplace=True)
print(student)
print()

# using read_csv

movies = pd.read_csv('Pandas/Pandas_DataFrame/movies.csv')
print(movies)
print()

ipl = pd.read_csv('Pandas/Pandas_DataFrame/ipl-matches.csv')
print(ipl)
print()


# DataFrame Attributes and methods

# shape

print(ipl.shape)
print(ipl.shape)
print(students.shape)
print()

# dtypes

print(movies.dtypes)
print(ipl.dtypes)
print(students.dtypes)
print()

# index

print(ipl.index)
print(students.index)
print()

# columns

print(movies.columns)
print(students.columns)
print()

# values

print(ipl.values)
print(students.values)

# methods

# head/tail

print(ipl.head())
print(ipl.head(2))
print(movies.tail())
print(movies.tail(2))
print(students.head(2))
print(students.tail(2))
print()

# sample

print(movies.sample(5))
print(ipl.sample(5))
print(students.sample(2))
print()

# info

print(ipl.info())
print(students.info())
print()

# describe

print(movies.describe())
print(students.describe())
print()

# isnull

print(movies.isnull().sum())
print(students.isnull().sum())
print()

# duplicated

print(movies.duplicated().sum())
print(ipl.duplicated().sum())
print()

# rename

print(students.rename(columns={'marks':'percent', 'package' : 'lpa'}))   # this is temporary for parmanent change use {inplace = True}
print()

# Mathematical methods

# sum, max, min, std, median, mean, var

print('sum\n',students.sum())
print('mean\n',students.mean())
print('median\n',students.median())
print('max\n',students.max())
print('min\n',students.min())
print('std\n',students.std())
print('var\n',students.var())
print()

# selecting cols from dataframes

# to fetch single col

print(movies['title_x'])
print(type(movies['title_x']))
print(ipl['Venue'])
print(type(ipl['Venue']))
print()

# to fetch multiple cols -> using fancy indexing

print(ipl[['Team1', 'Team2', 'WinningTeam', 'Player_of_Match']])
print()

# Selecting rows from dataframes
# using iloc and loc

# using iloc

print(movies.iloc[0])
print(student.iloc[0])
print()

print(movies.iloc[0:5])
print(movies.iloc[5:16:2])
print(students.iloc[[0,2,3]])
print()


# using loc

print(student.loc['Ram'])
print(student.loc['Ram':'Mohan'])
print(student.loc[['Ram', 'Kiran', 'Mohan']])
