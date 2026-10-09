# Pandas Learning

A personal learning repository for understanding and practicing **Pandas** for data analysis with Python.

---

## Day 1 — Pandas Basics

### 1. What is Pandas?

**Pandas** is a Python library used for:

* Data manipulation
* Data analysis
* Working with structured/tabular data
* Cleaning and transforming datasets

The two main Pandas data structures are:

* **Series** → 1-dimensional
* **DataFrame** → 2-dimensional

---

## 2. Pandas Series

A **Series** is a one-dimensional labeled data structure.

### Import Pandas

```python
import pandas as pd
```

### Series from a List

```python
s = pd.Series([10, 20, 30, 40])
```

Pandas automatically assigns an integer index starting from `0`.

### Series with Strings

```python
s = pd.Series(["Python", "Pandas", "NumPy"])
```

### Series with Custom Index

```python
s = pd.Series(
    [90, 85, 95],
    index=["Math", "Science", "English"]
)
```

### Setting a Name

```python
s = pd.Series(
    [90, 85, 95],
    index=["Math", "Science", "English"],
    name="Marks"
)
```

The `name` attribute gives a meaningful name to the Series.

### Series from a Dictionary

```python
marks = {
    "Math": 90,
    "Science": 85,
    "English": 95
}

s = pd.Series(marks)
```

Dictionary **keys become the index** and **values become the data**.

---

## Quick Revision

| Concept             | Key Point                        |
| ------------------- | -------------------------------- |
| Pandas              | Python library for data analysis |
| Series              | 1D labeled data structure        |
| `pd.Series()`       | Creates a Series                 |
| List → Series       | Values get default integer index |
| Custom index        | Set using `index=`               |
| Series name         | Set using `name=`                |
| Dictionary → Series | Keys → index, values → data      |

---

# Day 2 — Series from CSV & Series Methods

## 1. Creating Series from CSV

A Series can be created by reading a CSV file using `read_csv()` and converting the resulting DataFrame using `squeeze()`.

```python
import pandas as pd

subs = pd.read_csv("subs.csv").squeeze()
```

### CSV with an index column

```python
vk = pd.read_csv(
    "kohli_ipl.csv",
    index_col="match_no"
).squeeze()
```

`index_col` → specifies which CSV column should become the Series index.

`squeeze()` → converts a single-column DataFrame into a Series.

---

## 2. Series Methods

### `head()`

Returns the first 5 values by default.

```python
vk.head()
vk.head(10)
```

### `tail()`

Returns the last 5 values by default.

```python
subs.tail()
subs.tail(10)
```

### `sample()`

Returns random values from the Series.

```python
bwood.sample()
bwood.sample(5)
```

### `value_counts()`

Counts how many times each unique value occurs.

```python
bwood.value_counts()
```

Useful for understanding the frequency of categorical values.

### `sort_values()`

Sorts the Series based on its values.

```python
vk.sort_values()
vk.sort_values(ascending=False)
```

`ascending=False` → sorts in descending order.

### `sort_index()`

Sorts the Series based on its index.

```python
bwood.sort_index()
```

---

## Quick Revision

| Method           | Purpose                                   |
| ---------------- | ----------------------------------------- |
| `head()`         | First values                              |
| `tail()`         | Last values                               |
| `sample()`       | Random values                             |
| `value_counts()` | Frequency of unique values                |
| `sort_values()`  | Sort by values                            |
| `sort_index()`   | Sort by index                             |
| `squeeze()`      | Convert single-column DataFrame to Series |
| `index_col`      | Set a column as index                     |

---

# Day 3 — Series Indexing, Editing & Boolean Indexing

## 1. Series Indexing

Accessing values from a Series using its position or label.

### Integer Indexing

```python
s[0]
s[2]
```

### Negative Indexing

Access values from the end.

```python
s[-1]
```

### Slicing

```python
s[1:4]
```

### Negative Slicing

```python
s[-3:]
```

### Fancy Indexing

Access multiple specific positions.

```python
s[[0, 2, 4]]
```

### Label Indexing

Access values using their index labels.

```python
s["Math"]
```

---

## 2. Editing a Series

### Using Indexing

```python
s[0] = 100
```

### Editing Multiple Items

```python
s[0:3] = 100
```

### Fancy Indexing

```python
s[[0, 2]] = 100
```

### Using Index Labels

```python
s["Math"] = 95
```

If the specified label does not exist, assigning it can create a **new index entry**.

---

## 3. Series with Python Functions

Common Python functionality that works with Series:

```python
len(s)
type(s)
dir(s)

sorted(s)
min(s)
max(s)

list(s)
tuple(s)
```

### Membership

```python
10 in s
```

Checks the **index** by default.

### Looping

```python
for value in s:
    print(value)
```

### Arithmetic Operators

Operations can be performed directly on Series:

```python
s + 10
s * 2
s / 2
```

### Relational Operators

```python
s > 50
s == 100
s < 50
```

These return a Boolean Series.

---

## 4. Boolean Indexing

Boolean conditions can be used to filter a Series.

Example: finding Kohli's scores of `50` and above:

```python
vk[vk >= 50]
```

Finding the number of scores equal to `50` or `100`:

```python
(vk == 50).sum()
(vk == 100).sum()
```

Finding the number of ducks:

```python
(vk == 0).sum()
```

### Important Pattern

```python
s[condition]
```

→ filters the Series based on the condition.

---

## 5. Plotting Series

A Series can be visualized using:

### Line Plot

```python
vk.plot(kind="line")
```

### Bar Plot

```python
vk.plot(kind="bar")
```

### Pie Chart

```python
vk.plot(kind="pie")
```

These can be used to visualize patterns in Kohli's IPL match scores.

---

## Dataset Used

**Kohli IPL dataset** containing:

* Match number
* Runs scored by Virat Kohli in each IPL match

Used for practicing indexing, editing, filtering and visualization.

---

## Quick Revision

| Concept           | Key Point                          |
| ----------------- | ---------------------------------- |
| Integer indexing  | Access by position                 |
| Negative indexing | Access from the end                |
| Slicing           | Access a range                     |
| Fancy indexing    | Access multiple selected positions |
| Label indexing    | Access using index labels          |
| Boolean indexing  | Filter using conditions            |
| `len()`           | Number of elements                 |
| `sorted()`        | Sorted values                      |
| `min()` / `max()` | Minimum / maximum                  |
| Arithmetic        | Perform calculations on Series     |
| Relational        | Create Boolean conditions          |
| `plot()`          | Visualize Series                   |

---

## Day 4 — Important Series Methods

### 1. `astype()`

Converts Series values to a specified data type.

```python
vk.astype('int16')
```

### 2. `between()`

Checks whether values fall within a specified range (inclusive by default).

```python
vk[vk.between(49, 69)]
vk[vk.between(49, 69)].size
```

### 3. `clip()`

Limits values to a specified minimum and maximum. Values outside the range are replaced by the nearest boundary.

```python
subs.clip(100, 200)
```

### 4. `drop_duplicates()`

Removes duplicate values from a Series.

```python
temp.drop_duplicates()
temp.drop_duplicates(keep='last')
```

* Default: keeps the first occurrence.
* `keep='last'`: keeps the last occurrence.

### 5. `duplicated()`

Returns a Boolean Series indicating duplicate values.

```python
temp.duplicated()
temp.duplicated().sum()
```

By default, the first occurrence is marked `False`, and subsequent duplicates are marked `True`.

### 6. `isnull()`

Identifies missing values (`NaN`).

```python
temp.isnull()
temp.isnull().sum()
```

### 7. `dropna()`

Removes missing values from a Series.

```python
temp.dropna()
```

### 8. `fillna()`

Replaces missing values with a specified value.

```python
temp.fillna(temp.mean())
```

Here, missing values are replaced with the Series mean, calculated while ignoring missing values.

### 9. `isin()`

Checks whether each value belongs to a specified collection.

```python
vk[vk.isin([49, 99])]
```

Returns Kohli's scores that are either `49` or `99`.

### 10. `apply()`

Applies a function to each element of a Series.

```python
vk.apply(lambda x: 'good day' if x > vk.mean() else 'bad day')
```

Classifies each score as `good day` or `bad day` based on whether it is above the mean.

### 11. `copy()`

Creates a separate copy of a Series.

```python
new = vk.head().copy()
new[1] = 100

print(new)
print(vk)
```

Changes to `new` do not affect the original Series `vk`.

---

### Quick Revision

| Method              | Purpose                                  |
| ------------------- | ---------------------------------------- |
| `astype()`          | Convert data type                        |
| `between()`         | Check whether values fall within a range |
| `clip()`            | Limit values to a range                  |
| `drop_duplicates()` | Remove duplicate values                  |
| `duplicated()`      | Identify duplicate values                |
| `isnull()`          | Detect missing values                    |
| `dropna()`          | Remove missing values                    |
| `fillna()`          | Replace missing values                   |
| `isin()`            | Check membership in a collection         |
| `apply()`           | Apply a function to each element         |
| `copy()`            | Create an independent copy               |

---
