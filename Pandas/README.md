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

