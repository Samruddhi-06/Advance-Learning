import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Important dataframe methods

# valie_counts

ipl = pd.read_csv('Pandas/Pandas_DataFrame/ipl-matches.csv')

marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,80,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])

print(marks.value_counts())
print()

# find which player has won most potm in final and qualifier

print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())
print()

# toss decision plot -> pie chart of bat and field

ipl['TossDecision'].value_counts().plot(kind='pie')
# plt.show()

# how many matches each team has played

# pd.set_option('display.max_columns', None)
print((ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending=False))
print()

# sort_values -> ascending, na_position, inplace, multiple_cols

movies = pd.read_csv('Pandas/Pandas_DataFrame/movies.csv')
print(movies.sort_values('title_x'))
print(movies.sort_values('title_x',ascending=False))
print()

students = pd.DataFrame(
    {
        'name': ['nitish', 'Raman', 'Kishan', 'Ram', 'Ankit', np.nan],
        'college': ['vit', 'iit', np.nan, np.nan,'visi', np.nan],
        'branch': ['eee','it','cse',np.nan,'civ',np.nan],
        'cgpa': [8,4,3,np.nan,8,np.nan],
        'package': [10,4,2.2,np.nan,8.5,np.nan]
    }
)
print(students.sort_values('name'))
print()
print(students.sort_values('name',na_position='first'))
print()
print(students.sort_values('name',na_position='first', ascending=False))
print()

print(movies.sort_values(['year_of_release', 'title_x']).head())
print()
print(movies.sort_values(['year_of_release', 'title_x'],ascending=[True,False]).head())
print()

# rank

batsman = pd.read_csv('Pandas/Pandas_DataFrame/batsman_runs_ipl.csv')

print(batsman)
batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
print(batsman.sort_values('batting_rank'))