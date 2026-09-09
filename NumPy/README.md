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
