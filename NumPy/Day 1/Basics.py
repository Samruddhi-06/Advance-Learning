# creating a numpy array (ndarray)

import numpy as np

# 1D array -> Vector

a = np.array([1,2,3])
print("1D array :-")
print(a)
print(type(a))


# 2D array -> Matrix

b = np.array([[1,2,3],[4,5,6]],dtype=float)
print("2D array :-")
print(b)


# 3D array -> Tensor

c = np.array([[[1,2],[3,4],[5,6]]],dtype=float)
print("3D array :-")
print(c)


# different data type array

print("----------------------")

print("Floating dtype :-")
print(np.array([1,2,3], dtype=float))
print("Boolean dtype :-")
print(np.array([1,2,3], dtype=bool))
print("Complex dtype :-")
print(np.array([1,2,3], dtype=complex))

print("---------------------")

# np.arange

print(np.arange(1,11))
print(np.arange(1,11,2))

# np.arange with reshape

print(np.arange(1,11).reshape(5,2))
print(np.arange(1,13).reshape(4,3))

# np.ones and np.zeros

print(np.ones((3,3)))
print(np.zeros((3,4)))

# np.random

print(np.random.random((3,3)))

# np.linspace

print(np.linspace(-10,12,10))

# np.identity

print(np.identity(4))


print("--------------------")

# Array attributes

# ndim

print(a.ndim)
print(b.ndim)
print(c.ndim)


# shape

print(a.shape)
print(b.shape)
print(c.shape)

# size

print(a.size)
print(b.size)
print(c.size)

# itemsize

print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# dtype

print(a.dtype)
print(b.dtype)
print(c.dtype)


