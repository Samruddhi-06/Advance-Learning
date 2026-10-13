## Day 5 — Pandas DataFrame

### 1. What is a DataFrame?

A **DataFrame** is a two-dimensional tabular data structure containing rows and columns. It can store different data types in different columns.

### 2. Creating DataFrames

**Using a 2D list**
```python
students = pd.DataFrame(
    [[100, 80, 10], [90, 70, 7]],
    columns=['iq', 'marks', 'package']
)
```

**Using a dictionary**
```python
student = pd.DataFrame({
    'name': ['Ram', 'Shyam'],
    'marks': [80, 70]
})
```

**Using CSV**
```python
movies = pd.read_csv('movies.csv')
```

Set a column as the index:
```python
student.set_index('name', inplace=True)
```

### 3. DataFrame Attributes

| Attribute | Purpose |
|---|---|
| `df.shape` | Number of rows and columns |
| `df.dtypes` | Data type of each column |
| `df.index` | Row index labels |
| `df.columns` | Column names |
| `df.values` | Underlying data as an array |

### 4. Important DataFrame Methods

| Method | Purpose |
|---|---|
| `df.head()` | First 5 rows |
| `df.tail()` | Last 5 rows |
| `df.sample(5)` | 5 random rows |
| `df.info()` | Column types, non-null counts and memory usage |
| `df.describe()` | Summary statistics for numeric columns by default |
| `df.isnull().sum()` | Missing values in each column |
| `df.duplicated().sum()` | Number of duplicate rows |
| `df.rename()` | Rename rows or columns |
| `df.dropna()` | Remove missing data |

Use `inplace=True` with supported methods when you want to modify the original DataFrame.

### 5. Mathematical Methods

```python
df.sum()
df.mean()
df.median()
df.max()
df.min()
df.std()
df.var()
```

These calculate summary statistics, generally column-wise by default.

### 6. Selecting Columns

**Single column** — returns a Series:
```python
movies['title_x']
```

**Multiple columns** — returns a DataFrame:
```python
ipl[['Team1', 'Team2', 'WinningTeam']]
```

### 7. Selecting Rows: `iloc` and `loc`

**`iloc` — position-based selection**
```python
movies.iloc[0]          # First row
movies.iloc[0:5]        # First five rows
movies.iloc[0:3, 0:3]   # First 3 rows and columns
movies.iloc[[0, 2, 3]]  # Selected row positions
```

**`loc` — label-based selection**
```python
student.loc['Ram']
student.loc[['Ram', 'Shyam']]
```

Label-based slicing includes the ending label when it exists. Integer slicing with `iloc` excludes the ending position.

### 8. Filtering DataFrames

Filter rows using conditions.

**Find final match winners**
```python
ipl[ipl['MatchNumber'] == 'Final'][['Season', 'WinningTeam']]
```

**Count Super Over matches**
```python
ipl[ipl['SuperOver'] == 'Y'].shape[0]
```

**CSK wins in Kolkata**
```python
ipl[
    (ipl['City'] == 'Kolkata') &
    (ipl['WinningTeam'] == 'Chennai Super Kings')
].shape[0]
```

**Percentage of matches where toss winner also won**
```python
(ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]
 / ipl.shape[0]) * 100
```

**Movies with rating above 8 and more than 10,000 votes**
```python
movies[
    (movies['imdb_rating'] > 8) &
    (movies['imdb_votes'] > 10000)
]
```

For multiple conditions:
- `&` means AND
- `|` means OR
- Put each condition inside parentheses.

### 9. Filtering Text Data

Find Action movies with a rating above 7.5:

```python
mask1 = movies['genres'].str.split('|').apply(
    lambda x: 'Action' in x
)
mask2 = movies['imdb_rating'] > 7.5

movies[mask1 & mask2]
```

### 10. Writing Functions with DataFrames

A function can filter data and return useful results.

Example: head-to-head IPL records.

```python
def track_records(ipl, team1, team2):
    conditions = (
        ((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) |
        ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))
    )

    matches = ipl[conditions]

    return {
        'Total Matches': matches.shape[0],
        f'{team1} Wins': (
            matches[matches['WinningTeam'] == team1].shape[0]
        ),
        f'{team2} Wins': (
            matches[matches['WinningTeam'] == team2].shape[0]
        )
    }
```

### 11. Adding New Columns

**Add a constant column**
```python
movies['Country'] = 'India'
```

**Extract the lead actor**
```python
movies = movies.dropna(subset=['actors'])

movies['LeadActor'] = movies['actors'].str.split('|').apply(
    lambda x: x[0]
)
```

### 12. Changing Data Types

`astype()` converts a column to another data type.

```python
ipl['ID'] = ipl['ID'].astype('int32')

ipl['Season'] = ipl['Season'].astype('category')
ipl['Team1'] = ipl['Team1'].astype('category')
ipl['Team2'] = ipl['Team2'].astype('category')
```

- `int32`: 32-bit integer.
- `category`: useful for columns containing a limited set of repeated values, such as team names.

### Quick Revision

| Concept | Key Point |
|---|---|
| DataFrame | Two-dimensional tabular structure |
| `shape` | Rows and columns |
| `iloc` | Select by position |
| `loc` | Select by label |
| Boolean filtering | Select rows matching conditions |
| `str.split()` | Split text values |
| `apply()` | Apply a function along a Series or DataFrame axis |
| `dropna()` | Remove missing data |
| `astype()` | Change data types |
| `category` | Data type for categorical values |

---