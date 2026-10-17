## Day 5 — Important Pandas DataFrame Methods

### 1. `value_counts()`
Counts the frequency of unique values or rows.

```python
marks.value_counts()
ipl['Player_of_Match'].value_counts()
```

### 2. Plotting with `value_counts()`
Create a pie chart to visualize toss decisions.

```python
ipl['TossDecision'].value_counts().plot(kind='pie')
```

### 3. Counting Matches Played by Each Team
Combine the counts from `Team1` and `Team2`.

```python
(ipl['Team1'].value_counts() +
 ipl['Team2'].value_counts()).sort_values(ascending=False)
```

### 4. `sort_values()`
Sort rows based on one or more columns.

```python
movies.sort_values('title_x')
movies.sort_values('title_x', ascending=False)
```

**Important parameters:**
- `ascending=False` → descending order
- `na_position='first'` → place missing values first
- `inplace=True` → modify the original DataFrame
- Multiple columns → sort using more than one column

```python
movies.sort_values(['year_of_release', 'title_x'])
movies.sort_values(
    ['year_of_release', 'title_x'],
    ascending=[True, False]
)
```

### 5. `rank()`
Assigns ranks to values in a column.

```python
batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
```

Higher run totals receive better (lower numerical) ranks. By default, tied values receive their average rank.

### 6. `sort_index()`
Sorts rows using their index labels.

```python
movies.sort_index(ascending=False)
```

### 7. `set_index()`
Sets an existing column as the DataFrame index.

```python
batsman.set_index('batter')
```

Use `inplace=True` to modify the original DataFrame instead of returning a new one.

### 8. `reset_index()`
Moves the existing index back into a regular column and creates a default integer index.

```python
batsman.reset_index()
```

You can combine methods to replace the index:

```python
batsman.reset_index().set_index('batting_rank')
```

### 9. Series to DataFrame
Convert a Series into a DataFrame using `reset_index()`.

```python
marks_series.reset_index()
```

The result is a DataFrame containing the original index and values in separate columns.

### 10. `rename()`
Rename columns or index labels.

```python
movies.rename(columns={
    'imdb_id': 'imdb',
    'poster_path': 'link'
})
```

Rename index labels using `index=`.

### 11. `nunique()`
Counts the number of distinct, non-missing values.

```python
ipl['Umpire1'].nunique()
```

### 12. `isnull()` and `notnull()`
Identify missing and non-missing values.

```python
students.isnull()
students.notnull()
```

### 13. `dropna()`
Remove rows or columns containing missing values.

```python
students.dropna(how='any')
students.dropna(how='all')
students.dropna(subset=['name'])
students.dropna(subset=['name', 'college'])
```

- `how='any'` → drop a row if any selected value is missing.
- `how='all'` → drop a row only if all selected values are missing.
- `subset` → check only specified columns.

### 14. `fillna()`, `ffill()` and `bfill()`
Handle missing values by replacing or propagating values.

```python
students['name'].fillna('unknown')
students['name'].ffill()
students['name'].bfill()
```

- `fillna()` → replace missing values with a specified value.
- `ffill()` → fill using the previous valid value.
- `bfill()` → fill using the next valid value.

### 15. `drop_duplicates()`
Remove duplicate rows based on selected columns.

```python
ipl.drop_duplicates(
    subset=['City', 'did_vk_play'],
    keep='first'
)
```

- `keep='first'` → retain the first matching row.
- `keep='last'` → retain the last matching row.

### 16. `drop()`
Remove selected rows or columns.

```python
students.drop(columns=['branch', 'cgpa'])
students.drop(index=[0, 5])
```

### 17. `apply()`
Apply a custom function to rows or columns.

```python
points_df['Distance'] = points_df.apply(euclidean, axis=1)
```

- `axis=1` → apply the function row-wise.
- `axis=0` → apply the function column-wise (default).

**Example:** Calculate Euclidean distance between two points:

\[
d=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}
\]

---

### Quick Revision

| Method | Purpose |
|---|---|
| `value_counts()` | Count frequencies |
| `sort_values()` | Sort by column values |
| `rank()` | Assign ranks |
| `sort_index()` | Sort by index |
| `set_index()` | Set a column as index |
| `reset_index()` | Restore the index as a column |
| `rename()` | Rename columns or index labels |
| `nunique()` | Count distinct values |
| `isnull()` / `notnull()` | Detect missing/non-missing values |
| `dropna()` | Remove missing data |
| `fillna()` / `ffill()` / `bfill()` | Fill missing data |
| `drop_duplicates()` | Remove duplicate rows |
| `drop()` | Remove rows or columns |
| `apply()` | Apply a custom function |

---