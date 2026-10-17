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

# sort_index

print(movies.sort_index(ascending=False))
print()

# set_index

print(batsman.set_index('batter'))
print(batsman.set_index('batter',inplace=True))

# reset_index

print(batsman.reset_index())

# how to replace existing index without loosing

print(batsman.reset_index().set_index('batting_rank'))

# series to dataframe

marks = {
    'maths': 97,
    'science': 57,
    'english': 83,
    'hindi': 100
}
marks_series = pd.Series(marks)
print(marks_series)
print(marks_series.reset_index())
print(type(marks_series.reset_index()))


# rename

print(movies.set_index('title_x'))
print(movies.rename(columns = {'imdb_id':'imdb', 'poster_path':'link'}))

# we can also rename index

movies = movies.rename(index={'Uri: The Surgical Strike': 'Uri', 'Battalion 609': 'Battalion'})
print(movies)

# nunique

print(ipl['Umpire1'].nunique())

# isnull
print(students.isnull())
print()
print(students.notnull())
print()

# dropna

print(students.dropna(how='any'))
print()
print(students.dropna(how='all'))
print()

# we can also give subset values

print(students.dropna(subset = ['name']))
print()
print(students.dropna(subset = ['name','college']))
print()

# fillna

print(students['name'].fillna('unknown'))
print()
# using paramenter like method = 'ffill' or 'bfill'
print(students['name'].ffill())
print()
print(students['name'].bfill())
print()

# drop_duplicates

# find last match played by vk in delhi

print(ipl.head(2))

ipl['all_players'] = ipl['Team1Players'] + ipl['Team2Players']

def did_vk_play(all_players):
    return 'V Kohli' in all_players

ipl['did_vk_play'] = ipl['all_players'].apply(did_vk_play)
print(ipl[(ipl['City'] == 'Delhi') & (ipl['did_vk_play'] == True)].drop_duplicates(subset = ['City','did_vk_play'],keep='first'))
print()

# drop

print(students.drop(columns = ['branch', 'cgpa']))
print(students.drop(index = [0,5]))
print()

# apply

points_df = pd.DataFrame (
    {
        '1stpoint': [(3,4),(0,0),(7,6),(4,8)],
        '2ndpoint': [(-3,4),(0,0),(-5,-6),(4,-9)]
    }
)

print(points_df)
print()

def euclidean(row):
    pt_A = row['1stpoint']
    pt_B = row['2ndpoint']

    return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5

points_df['Distance'] = points_df.apply(euclidean,axis=1)
print(points_df)