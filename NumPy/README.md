# NumPy

NumPy (Numerical Python) is a Python library used for **numerical computing**. It provides powerful multidimensional arrays and functions for performing mathematical and numerical operations efficiently.

NumPy is widely used in **Data Analytics, Data Science, Machine Learning, Scientific Computing**, and other fields involving numerical data.

---

## Day 1

### 1. What is NumPy?

NumPy stands for **Numerical Python**.

The main object in NumPy is the **`ndarray` (N-dimensional array)**. It allows us to store and work with collections of numerical data efficiently.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

NumPy arrays can be **1-dimensional, 2-dimensional, 3-dimensional, or higher-dimensional**.

---

### 2. NumPy vs Python Sequences

Python provides built-in sequences such as **lists and tuples**, while NumPy provides specialized arrays for numerical operations.

| Python List                                 | NumPy Array                                   |
| ------------------------------------------- | --------------------------------------------- |
| General-purpose data structure              | Designed for numerical computing              |
| Can contain different data types            | Usually stores elements of the same data type |
| Mathematical operations are less convenient | Supports vectorized mathematical operations   |
| Generally uses more memory                  | More memory-efficient for numerical data      |
| Slower for large numerical operations       | Faster for numerical operations               |

Example:

```python
# Python list
numbers = [1, 2, 3, 4]

# NumPy array
numbers = np.array([1, 2, 3, 4])
```

NumPy arrays are especially useful when working with **large amounts of numerical data**.

---

# 3. Creating NumPy Arrays

### `np.array()`

Creates a NumPy array from a Python sequence.

```python
arr = np.array([1, 2, 3, 4])
```

### 2D Array

A 2D array consists of rows and columns.

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
```

### 3D Array

A 3D array consists of multiple 2D arrays.

```python
arr = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]])
```

### Specifying Data Type

The `dtype` parameter can be used to specify the data type of an array.

```python
arr = np.array([1, 2, 3], dtype=float)
```

---

### `np.arange()`

Creates an array containing evenly spaced values within a given range.

```python
arr = np.arange(1, 10)
```

It works similarly to Python's `range()`, but returns a NumPy array.

### `np.arange()` with `reshape()`

`reshape()` changes the shape of an array without changing its data.

```python
arr = np.arange(1, 13).reshape(3, 4)
```

This creates a **3 × 4** array.

---

### `np.ones()`

Creates an array filled with ones.

```python
arr = np.ones((2, 3))
```

### `np.zeros()`

Creates an array filled with zeros.

```python
arr = np.zeros((2, 3))
```

### `np.random`

The `np.random` module provides functions for generating random values.

```python
arr = np.random.rand(2, 3)
```

It can be useful when generating random numerical data for testing, simulations, and other applications.

### `np.linspace()`

Creates evenly spaced numbers between a start and end value.

```python
arr = np.linspace(1, 10, 5)
```

Here, NumPy generates **5 evenly spaced values** between 1 and 10.

### `np.identity()`

Creates a square identity matrix with ones on the main diagonal and zeros elsewhere.

```python
arr = np.identity(3)
```

Output:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

# 4. Array Attributes

NumPy arrays have several important attributes that provide information about the array.

### `ndim`

Returns the **number of dimensions** of the array.

```python
arr.ndim
```

### `shape`

Returns the **size of the array along each dimension**.

```python
arr.shape
```

For a 2D array with 3 rows and 4 columns:

```text
(3, 4)
```

### `size`

Returns the **total number of elements** in the array.

```python
arr.size
```

### `itemsize`

Returns the **number of bytes occupied by each element**.

```python
arr.itemsize
```

The value depends on the array's data type.

### `dtype`

Returns the **data type of the elements** in the array.

```python
arr.dtype
```

---

## Quick Reference

| Function / Attribute | Purpose                        |
| -------------------- | ------------------------------ |
| `np.array()`         | Create an array                |
| `np.arange()`        | Create values within a range   |
| `reshape()`          | Change array shape             |
| `np.ones()`          | Create an array of ones        |
| `np.zeros()`         | Create an array of zeros       |
| `np.random`          | Generate random values         |
| `np.linspace()`      | Generate evenly spaced values  |
| `np.identity()`      | Create an identity matrix      |
| `ndim`               | Number of dimensions           |
| `shape`              | Dimensions of the array        |
| `size`               | Total number of elements       |
| `itemsize`           | Bytes occupied by each element |
| `dtype`              | Data type of elements          |

---

## Day 2

### 1. Changing Data Type — `astype()`

The `astype()` method is used to **convert a NumPy array from one data type to another**.

```python
arr = np.array([1, 2, 3])
new_arr = arr.astype(float)
```

The original array is not changed; `astype()` returns a new array with the specified data type.

---

# 2. Array Operations

NumPy allows mathematical and comparison operations to be performed directly on arrays.

### Scalar Operations

A **scalar operation** applies a single value to every element of the array.

#### Arithmetic Operations

```python
arr = np.array([1, 2, 3, 4])

arr + 2
arr - 2
arr * 2
arr / 2
arr ** 2
```

The operation is performed element-wise.

#### Relational Operations

Relational operators compare each element with a value and return a Boolean array.

```python
arr > 2
arr == 2
arr <= 3
```

---

### Vector Operations

A **vector operation** performs an operation between corresponding elements of two arrays.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b
a * b
```

The operation is performed element by element.

---

# 3. NumPy Array Functions

NumPy provides many built-in functions for performing calculations on arrays.

### Minimum, Maximum, Sum and Product

```python
np.min(arr)
np.max(arr)
np.sum(arr)
np.prod(arr)
```

* `np.min()` → smallest element
* `np.max()` → largest element
* `np.sum()` → sum of all elements
* `np.prod()` → product of all elements

---

### Mean, Median, Standard Deviation and Variance

```python
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
```

* `np.mean()` → arithmetic average
* `np.median()` → middle value after sorting
* `np.std()` → standard deviation
* `np.var()` → variance

These functions are particularly useful when working with **statistical and analytical data**.

---

### Trigonometric Functions

NumPy provides trigonometric functions such as:

```python
np.sin(arr)
np.cos(arr)
np.tan(arr)
```

These functions operate element-wise on the array.

---

### Logarithmic and Exponential Functions

```python
np.log(arr)
np.exp(arr)
```

* `np.log()` → natural logarithm
* `np.exp()` → exponential function

NumPy also provides other logarithmic functions such as `np.log10()`.

---

### Dot Product

The `np.dot()` function calculates the **dot product** of two arrays.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)
```

For 1D arrays, it calculates the sum of the products of corresponding elements.

---

### Rounding Functions

NumPy provides functions for rounding numbers.

```python
np.round(arr)
np.floor(arr)
np.ceil(arr)
```

* `np.round()` → rounds to the nearest value
* `np.floor()` → rounds down to the nearest integer
* `np.ceil()` → rounds up to the nearest integer

---

# Quick Reference

| Function / Method        | Purpose                |
| ------------------------ | ---------------------- |
| `astype()`               | Change array data type |
| `+`, `-`, `*`, `/`, `**` | Arithmetic operations  |
| `>`, `<`, `==`, `!=`     | Relational operations  |
| `np.min()`               | Minimum value          |
| `np.max()`               | Maximum value          |
| `np.sum()`               | Sum of elements        |
| `np.prod()`              | Product of elements    |
| `np.mean()`              | Mean                   |
| `np.median()`            | Median                 |
| `np.std()`               | Standard deviation     |
| `np.var()`               | Variance               |
| `np.sin()`               | Sine                   |
| `np.cos()`               | Cosine                 |
| `np.tan()`               | Tangent                |
| `np.log()`               | Natural logarithm      |
| `np.exp()`               | Exponential            |
| `np.dot()`               | Dot product            |
| `np.round()`             | Round values           |
| `np.floor()`             | Round down             |
| `np.ceil()`              | Round up               |


---

## Day 3

# 1. Indexing and Slicing

**Indexing** is used to access individual elements of a NumPy array, while **slicing** is used to access a range of elements.

### 1D Array

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]       # 10
arr[-1]      # 50
arr[1:4]     # [20 30 40]
```

### 2D Array

For a 2D array, indexing uses **row and column** positions.

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr[0, 1]       # 2
arr[1, 2]       # 6
arr[0, :]       # First row
arr[:, 1]       # Second column
```

### 3D Array

For a 3D array, indexing uses **layer, row, and column** positions.

```python
arr = np.array([[[1, 2],
                 [3, 4]],

                [[5, 6],
                 [7, 8]]])

arr[0, 1, 0]    # 3
```

The general indexing pattern is:

```text
1D → array[index]
2D → array[row, column]
3D → array[layer, row, column]
```

---

# 2. Iteration

Iteration means accessing the elements of an array one by one.

### Iterating a 1D Array

```python
for x in arr:
    print(x)
```

### Iterating a 2D Array

A normal loop iterates through the rows first.

```python
for row in arr:
    print(row)
```

Nested loops can be used to access individual elements.

```python
for row in arr:
    for x in row:
        print(x)
```

### Iterating a 3D Array

For higher-dimensional arrays, nested loops can be used for each dimension.

```python
for layer in arr:
    for row in layer:
        for x in row:
            print(x)
```

### `np.nditer()`

`np.nditer()` provides an easy way to iterate over **every element**, regardless of the number of dimensions.

```python
for x in np.nditer(arr):
    print(x)
```

---

# 3. Reshaping

Reshaping changes the arrangement or shape of an array without changing its elements.

### `np.transpose()`

`np.transpose()` swaps the axes of an array. For a 2D array, it effectively changes rows into columns and columns into rows.

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

np.transpose(arr)
```

The `T` attribute can also be used:

```python
arr.T
```

### `ravel()`

`ravel()` converts a multidimensional array into a **1D array**.

```python
arr = np.array([[1, 2],
                [3, 4]])

arr.ravel()
```

Output:

```text
[1 2 3 4]
```

---

# 4. Stacking

Stacking is used to **combine multiple arrays** into a single array.

### `np.hstack()`

`hstack()` stacks arrays **horizontally**, along columns.

```python
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

np.hstack((a, b))
```

### `np.vstack()`

`vstack()` stacks arrays **vertically**, along rows.

```python
np.vstack((a, b))
```

For stacking to work, the arrays must have compatible shapes.

---

# 5. Splitting

Splitting divides one array into multiple smaller arrays.

### `np.hsplit()`

`hsplit()` splits an array **horizontally**, dividing it along the columns.

```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

np.hsplit(arr, 2)
```

### `np.vsplit()`

`vsplit()` splits an array **vertically**, dividing it along the rows.

```python
np.vsplit(arr, 2)
```

The array must have a compatible number of rows or columns for the requested split.

---

# Quick Reference

| Function / Concept | Purpose                        |
| ------------------ | ------------------------------ |
| `arr[index]`       | Access elements using indexing |
| `arr[start:stop]`  | Slice an array                 |
| `np.nditer()`      | Iterate through every element  |
| `np.transpose()`   | Transpose / rearrange axes     |
| `arr.T`            | Shortcut for transpose         |
| `arr.ravel()`      | Flatten array into 1D          |
| `np.hstack()`      | Stack arrays horizontally      |
| `np.vstack()`      | Stack arrays vertically        |
| `np.hsplit()`      | Split array horizontally       |
| `np.vsplit()`      | Split array vertically         |


---

## Day 4 — Advanced Concepts

# 1. Broadcasting

**Broadcasting** is NumPy's mechanism for performing operations on arrays with different shapes, without explicitly reshaping or copying the smaller array.

For example:

```python
arr = np.array([1, 2, 3])
arr + 10
```

Output:

```text
[11 12 13]
```

The scalar `10` is effectively applied to every element.

Broadcasting also works between compatible arrays:

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

a + b
```

Here, `b` is broadcast across each row of `a`.

### Broadcasting Rules

When NumPy compares two shapes, it starts from the **trailing (rightmost) dimensions**.

Two dimensions are compatible when:

1. They are equal, or
2. One of them is `1`.

For example:

```text
(2, 3)
(3,)
```

These shapes are compatible because the `(3,)` array can be broadcast across the rows.

However:

```text
(2, 3)
(2,)
```

is not compatible because the dimensions do not satisfy the broadcasting rules.

Broadcasting is important because it allows operations between arrays of compatible shapes without manually duplicating data.

---

# 2. Working with Mathematical Formulas

NumPy makes it convenient to implement mathematical formulas using arrays.

## Sigmoid Function

The **sigmoid function** maps a value to a range between 0 and 1.

Formula:

```text
σ(x) = 1 / (1 + e⁻ˣ)
```

In NumPy:

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

The sigmoid function is commonly encountered in **machine learning**, particularly in binary classification.

---

## Mean Squared Error (MSE)

Mean Squared Error measures the average squared difference between actual and predicted values.

Formula:

```text
MSE = (1/n) Σ(y_actual - y_predicted)²
```

Using NumPy:

```python
def mse(y_actual, y_predicted):
    return np.mean((y_actual - y_predicted) ** 2)
```

A smaller MSE means the predictions have smaller squared errors relative to the actual values.

---

## Binary Cross Entropy (BCE)

Binary Cross Entropy is a loss function commonly used for **binary classification**.

Formula:

```text
BCE = -1/n Σ[y log(p) + (1-y) log(1-p)]
```

where:

* `y` → actual binary value
* `p` → predicted probability
* `n` → number of observations

A NumPy implementation can be written as:

```python
def binary_cross_entropy(y, p):
    return -np.mean(
        y * np.log(p) + (1 - y) * np.log(1 - p)
    )
```

In practical implementations, predicted probabilities are usually kept away from exactly `0` and `1` to avoid taking `log(0)`.

---

# 3. Working with Missing Values

NumPy can represent missing numerical values using `np.nan` (**Not a Number**).

```python
arr = np.array([10, 20, np.nan, 40])
```

### Detecting Missing Values

```python
np.isnan(arr)
```

This returns a Boolean array indicating which elements are `NaN`.

### Counting Missing Values

```python
np.sum(np.isnan(arr))
```

### Ignoring Missing Values in Calculations

Regular aggregation functions such as `np.mean()` return `nan` when the array contains a `NaN`.

```python
np.mean(arr)
```

NumPy provides `nan`-aware functions to ignore missing values:

```python
np.nanmean(arr)
np.nansum(arr)
np.nanmin(arr)
np.nanmax(arr)
```

For example:

```python
np.nanmean(arr)
```

calculates the mean while ignoring `NaN` values.

---

# 4. Graph Plotting

NumPy can be combined with **Matplotlib** to generate mathematical plots.

```python
import numpy as np
import matplotlib.pyplot as plt
```

The general process is:

```python
x = np.linspace(-10, 10, 100)

y = ...
plt.plot(x, y)
plt.show()
```

The `x` values provide the input, while the calculated `y` values determine the curve.

---

## `y = x`

```python
x = np.linspace(-10, 10, 100)
y = x

plt.plot(x, y)
plt.show()
```

This produces a straight line.

---

## `y = x²`

```python
x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y)
plt.show()
```

This produces a **parabolic curve**.

---

## `y = sin(x)`

```python
x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

`np.sin()` uses **radians** for its input.

---

## `y = x log(x)`

For the natural logarithm:

```python
x = np.linspace(0.1, 10, 100)
y = x * np.log(x)

plt.plot(x, y)
plt.show()
```

The values start above zero because `log(x)` is defined for positive real `x`.

---

## Sigmoid Curve

```python
x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

plt.plot(x, y)
plt.show()
```

This produces the characteristic **S-shaped sigmoid curve**, with values approaching 0 for large negative inputs and 1 for large positive inputs.

---

# Quick Reference

| Concept / Function | Purpose                                                       |
| ------------------ | ------------------------------------------------------------- |
| Broadcasting       | Perform operations on compatible arrays with different shapes |
| `np.exp()`         | Exponential function                                          |
| `np.mean()`        | Calculate mean                                                |
| `np.isnan()`       | Detect `NaN` values                                           |
| `np.nanmean()`     | Mean while ignoring `NaN`                                     |
| `np.nansum()`      | Sum while ignoring `NaN`                                      |
| `np.nanmin()`      | Minimum while ignoring `NaN`                                  |
| `np.nanmax()`      | Maximum while ignoring `NaN`                                  |
| `plt.plot()`       | Plot a graph                                                  |
| `plt.show()`       | Display the graph                                             |
| Sigmoid            | Maps values toward the range 0–1                              |
| MSE                | Measures mean squared prediction error                        |
| BCE                | Measures binary classification loss                           |

---

## Day 6 — Useful NumPy Functions

NumPy provides many functions for **sorting, searching, manipulating, aggregating, comparing, and analyzing arrays**.

# 1. Useful NumPy Functions

### `np.sort()`

Returns a sorted copy of an array.

```python
arr = np.array([4, 1, 3, 2])
np.sort(arr)
```

---

### `np.append()`

Appends values to the end of an array and returns a new array.

```python
arr = np.array([1, 2, 3])
np.append(arr, 4)
```

---

### `np.concatenate()`

Joins two or more arrays along an existing axis.

```python
a = np.array([1, 2])
b = np.array([3, 4])

np.concatenate((a, b))
```

Unlike `np.append()`, `concatenate()` is particularly useful when combining multiple arrays with compatible shapes.

---

### `np.unique()`

Returns the **unique elements** of an array, removing duplicates.

```python
arr = np.array([1, 2, 2, 3, 3, 3])
np.unique(arr)
```

---

### `np.expand_dims()`

Adds a new dimension to an array at the specified axis.

```python
arr = np.array([1, 2, 3])

np.expand_dims(arr, axis=0)
```

This is useful when you need to change the dimensionality of an array while preserving its data.

---

### `np.where()`

Returns the indices where a condition is `True`.

```python
arr = np.array([10, 20, 30, 40])

np.where(arr > 20)
```

It can also be used as a conditional expression:

```python
np.where(arr > 20, 1, 0)
```

---

### `np.argmax()`

Returns the **index of the maximum value**.

```python
arr = np.array([10, 50, 30])
np.argmax(arr)
```

### `np.argmin()`

Returns the **index of the minimum value**.

```python
np.argmin(arr)
```

---

### `np.cumsum()`

Returns the **cumulative sum** of elements.

```python
arr = np.array([1, 2, 3, 4])
np.cumsum(arr)
```

Output:

```text
[1 3 6 10]
```

### `np.cumprod()`

Returns the **cumulative product** of elements.

```python
np.cumprod(arr)
```

---

### `np.percentile()`

Calculates the value below which a given percentage of observations falls.

```python
arr = np.array([10, 20, 30, 40, 50])

np.percentile(arr, 50)
```

The 50th percentile corresponds to the median.

Percentiles are commonly used in **statistical analysis and exploratory data analysis**.

---

### `np.histogram()`

Computes the frequency distribution of data within specified bins.

```python
arr = np.array([1, 2, 2, 3, 4, 5])

np.histogram(arr)
```

It returns:

* The counts of values in each bin
* The boundaries of the bins

---

### `np.corrcoef()`

Calculates the **correlation coefficient matrix**.

```python
x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

np.corrcoef(x, y)
```

Correlation coefficients describe the **linear relationship** between variables, with values ranging from `-1` to `1`.

---

### `np.isin()`

Checks whether elements of an array are present in another set of values.

```python
arr = np.array([1, 2, 3, 4])

np.isin(arr, [2, 4])
```

It returns a Boolean array.

---

### `np.flip()`

Reverses the order of elements in an array.

```python
arr = np.array([1, 2, 3, 4])

np.flip(arr)
```

---

### `np.put()`

Replaces elements at specified indices with given values.

```python
arr = np.array([1, 2, 3, 4])

np.put(arr, [0, 2], [10, 30])
```

`np.put()` modifies the original array.

---

### `np.delete()`

Returns a new array with specified elements or indices removed.

```python
arr = np.array([1, 2, 3, 4])

np.delete(arr, 1)
```

The original array is not modified.

---

### `np.clip()`

Limits array values to a specified minimum and maximum range.

```python
arr = np.array([1, 5, 10, 15, 20])

np.clip(arr, 5, 15)
```

Values below `5` become `5`, and values above `15` become `15`.

---

# 2. Set Functions

NumPy provides functions for performing **set operations on arrays**.

These functions generally work with **1D arrays** and return sorted unique values.

### `np.union1d()`

Returns the unique values present in either of the two arrays.

```python
a = np.array([1, 2, 3])
b = np.array([3, 4, 5])

np.union1d(a, b)
```

Output:

```text
[1 2 3 4 5]
```

---

### `np.intersect1d()`

Returns the unique values that are present in **both arrays**.

```python
np.intersect1d(a, b)
```

Output:

```text
[3]
```

---

### `np.setdiff1d()`

Returns the values that are present in the first array but **not in the second**.

```python
np.setdiff1d(a, b)
```

Output:

```text
[1 2]
```

---

### `np.setxor1d()`

Returns the unique values that are present in **either array, but not in both**.

```python
np.setxor1d(a, b)
```

Output:

```text
[1 2 4 5]
```

---

# Quick Reference

| Function           | Purpose                              |
| ------------------ | ------------------------------------ |
| `np.sort()`        | Sort an array                        |
| `np.append()`      | Append values                        |
| `np.concatenate()` | Join arrays                          |
| `np.unique()`      | Find unique values                   |
| `np.expand_dims()` | Add a dimension                      |
| `np.where()`       | Find elements satisfying a condition |
| `np.argmax()`      | Index of maximum value               |
| `np.argmin()`      | Index of minimum value               |
| `np.cumsum()`      | Cumulative sum                       |
| `np.cumprod()`     | Cumulative product                   |
| `np.percentile()`  | Calculate percentile                 |
| `np.histogram()`   | Calculate frequency distribution     |
| `np.corrcoef()`    | Calculate correlation coefficients   |
| `np.isin()`        | Check membership                     |
| `np.flip()`        | Reverse an array                     |
| `np.put()`         | Replace values at indices            |
| `np.delete()`      | Delete elements                      |
| `np.clip()`        | Limit values to a range              |
| `np.union1d()`     | Union of two arrays                  |
| `np.intersect1d()` | Intersection of two arrays           |
| `np.setdiff1d()`   | Difference between arrays            |
| `np.setxor1d()`    | Symmetric difference                 |
