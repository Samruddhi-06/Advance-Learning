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


# selecting both rows and cols

# using iloc

print(movies.iloc[0:3,0:3])

# using loc

print(movies.loc[0:3, 'title_x':'poster_path'])

print()

# Filtering a dataframe

# find all the finale winners

pd.set_option('display.max_columns', None)
print(ipl.head(2))
new_df = ipl[ipl['MatchNumber'] == 'Final']
print(new_df[['Season', 'WinningTeam']])
print()

# how many superover finishes have occurred

print(ipl[ipl['SuperOver'] == 'Y'].shape[0])
print()

# how many matches has csk won in kolkata

print(ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])
print()

# toss winner is match winner in percentage

print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100)
print()

# movies with rating higher than 8 and votes > 10000

pd.set_option('display.max_columns', None)
print(movies.head(2))

print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000)].shape[0])
print()

# Action movies with rating higher than 7.5

mask1 = movies['genres'].str.split('|').apply(lambda x: 'Action' in x)
mask2 = movies['imdb_rating'] > 7.5
print(movies[mask1 & mask2].shape[0])
print()


# write a function that returns  the track record of 2 teams against each other

def track_records(ipl, team1, team2):
    conditions = (
        ((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) |
        ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))
    )

    h2h_matches = ipl[conditions]

    total_matches = h2h_matches.shape[0]

    team1_wins = h2h_matches[h2h_matches['WinningTeam'] == team1].shape[0]
    team2_wins = h2h_matches[h2h_matches['WinningTeam'] == team2].shape[0]

    return {
        'Total Matches': total_matches,
        f'{team1} Wins': team1_wins,
        f'{team2} Wins': team2_wins,
    }

csk_vs_mi = track_records(ipl, 'Chennai Super Kings', 'Mumbai Indians')
print(csk_vs_mi)
print()
csk_vs_rcb = track_records(ipl, 'Chennai Super Kings', 'Royal Challengers Bangalore')
print(csk_vs_rcb)

# Adding new cols

# completely new cols

movies['Country'] = 'India'
print((movies).head())

# existing ols

movies.dropna(subset=['actors'],inplace=True)

movies['LeadActor'] = movies['actors'].str.split('|').apply(lambda x:x[0])
print(movies.head())

# Important data functions

# astype

print(ipl.info())
ipl['ID'] = ipl['ID'].astype('int32')
print(ipl.info())
ipl['Season'] = ipl['Season'].astype('category')
print(ipl.info())
ipl['Team1'] = ipl['Team1'].astype('category')
ipl['Team2'] = ipl['Team2'].astype('category')
print(ipl.info())
print()