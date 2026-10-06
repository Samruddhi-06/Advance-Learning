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


