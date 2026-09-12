# Python sequence/lists VS numpy array

# 1. speed
# python

# l1 = [i for i in range(10000000)]
# l2 = [i for i in range(10000000, 20000000)]

# c1 = []

# import time
# start = time.time()
# for i in range(len(l1)):
#     c1.append(l1[i] + l2[i])

# print(time.time()-start)


# numpy

import numpy as np

# a1 = np.arange(10000000)
# a2 = np.arange(10000000, 20000000)

# start = time.time()
# c2 = a1 + a2

# print(time.time()-start)


# 2. Memory
# python

a = [i for i in range(10000000)]
import sys
print(sys.getsizeof(a))

# numpy

b = np.arange(10000000)
print(sys.getsizeof(b))

# Advanced indexing

# fancy indexing

# for 1d

a1 = np.array([1,2,3,4,5,6,7,8])
print(a1[[1,2,5,7]])

# for 2d

a2 = np.arange(12).reshape(4,3)
print("a2:-")
print(a2)
print("for rows:-")
print(a2[[0,2,3]])
print("for cols:-")
print(a2[:,[0,2]])

a3 = np.arange(24).reshape(6,4)
print("a3:-")
print(a3)
print(a3[[1,3,4]])
print(a3[:,[0,2,3]])