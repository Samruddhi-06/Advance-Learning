# Pandas DataFrame — Day 1

## 1. Creating DataFrames

A **DataFrame** is a 2-dimensional, tabular data structure with rows and columns.

### Using a 2D List

```python
student_data = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

students = pd.DataFrame(
    student_data,
    columns=['iq', 'marks', 'package']
)
```

### Using a Dictionary

```python
student = pd.DataFrame(student_dict)
student.set_index('name', inplace=True)
```

Dictionary keys become column names, and lists provide column values.

### Using CSV Files

```python
movies = pd.read_csv('Pandas/Pandas_DataFrame/movies.csv')
ipl = pd.read_csv('Pandas/Pandas_DataFrame/ipl-matches.csv')
```

`read_csv()` loads CSV data into a DataFrame.

---

## 2. DataFrame Attributes

| Attribute | Purpose |
|---|---|
| `df.shape` | Returns number of rows and columns |
| `df.dtypes` | Shows the data type of each column |
| `df.index` | Returns row index labels |
| `df.columns` | Returns column names |
| `df.values` | Returns the underlying data as an array |

Example:

```python
ipl.shape
ipl.dtypes
ipl.index
ipl.columns
ipl.values
```

---

## 3. DataFrame Methods

| Method | Purpose |
|---|---|
| `head()` | Returns first 5 rows by default |
| `tail()` | Returns last 5 rows by default |
| `sample(n)` | Returns `n` random rows |
| `info()` | Shows column types, non-null counts and memory usage |
| `describe()` | Generates descriptive statistics for numeric columns by default |
| `isnull().sum()` | Counts missing values in each column |
| `duplicated().sum()` | Counts duplicate rows |
| `rename()` | Renames row or column labels |

Examples:

```python
ipl.head(2)
movies.tail(2)
movies.sample(5)

ipl.info()
movies.describe()

movies.isnull().sum()
movies.duplicated().sum()

students.rename(
    columns={'marks': 'percent', 'package': 'lpa'}
)
```

**Note:** `rename()` returns a modified DataFrame without changing the original by default. Use `inplace=True` for an in-place change.

---

## 4. Mathematical Methods

These methods perform calculations on numeric columns by default.

```python
students.sum()
students.mean()
students.median()
students.max()
students.min()
students.std()
students.var()
```

| Method | Purpose |
|---|---|
| `sum()` | Sum of values |
| `mean()` | Average |
| `median()` | Middle value |
| `max()` | Maximum value |
| `min()` | Minimum value |
| `std()` | Standard deviation |
| `var()` | Variance |

---

## 5. Selecting Columns

### Single Column

```python
movies['title_x']
ipl['Venue']
```

Returns a **Series**.

```python
type(movies['title_x'])
```

### Multiple Columns — Fancy Indexing

```python
ipl[['Team1', 'Team2', 'WinningTeam', 'Player_of_Match']]
```

Returns a **DataFrame**.

**Remember:** Single column uses one pair of brackets; multiple columns use a list inside double brackets.

---

## 6. Selecting Rows

### Using `iloc` — Integer Position

Selects rows by their numerical positions.

```python
movies.iloc[0]          # First row
movies.iloc[0:5]        # Rows at positions 0–4
movies.iloc[5:16:2]     # Every second row from 5 to 15
students.iloc[[0, 2, 3]]  # Selected positions
```

### Using `loc` — Index Labels

Selects rows using index labels.

```python
student.loc['Ram']
student.loc['Ram':'Mohan']
student.loc[['Ram', 'Kiran', 'Mohan']]
```

**Important:** Label slicing with `loc` includes the ending label when it exists in the index. Position slicing with `iloc` excludes the ending position.

---

## Quick Revision

- **DataFrame:** 2-dimensional tabular structure.
- **Series:** A single column selected using `df['column']`.
- **Attributes:** `shape`, `dtypes`, `index`, `columns`, `values`.
- **Inspection:** `head()`, `tail()`, `sample()`, `info()`, `describe()`.
- **Data quality:** `isnull()`, `duplicated()`.
- **Statistics:** `sum()`, `mean()`, `median()`, `max()`, `min()`, `std()`, `var()`.
- **Selection:** `df['col']`, `df[['col1', 'col2']]`, `iloc`, `loc`.

---