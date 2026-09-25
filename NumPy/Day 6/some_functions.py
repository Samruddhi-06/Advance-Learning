import numpy as np

a = np.random.randint(1,100,24).reshape(6,4)
b = np.random.randint(1,100,24)

print("a: ",a)
print("b: ",b)

# 1. np.sort

print(np.sort(b)[::-1])
print()
print(np.sort(b))
print()

# 2. np.append

print(np.append(a,200))
print()
print(np.append(a,np.ones((a.shape[0],1)),axis=1))
print()

# 3.np.concatenate

c = np.arange(6,12).reshape(2,3)
d = np.arange(6).reshape(2,3)

print(np.concatenate((c,d), axis=0))
print(np.concatenate((c,d), axis=1))
print()

# 4. np.unique

x = np.array([1,2,3,1,2,3,1,1,2,3,4,5,6,6,6,5,4,5,2])
print(np.unique(x))
print()

# 5. np.expand_dims

print(np.expand_dims(b, axis=0))
print(np.expand_dims(a, axis=1))
print()

# 6. np.where

print(np.where(b > 55)) # give indx of ele
print()
print(np.where(a%2 == 0, 0, a))
print()

# 7. np.argmax & np.argmin

print(np.argmax(b))
print(np.argmax(a, axis=0))
print()
print(np.argmin(b))
print(np.argmin(a,axis=1))
print()

# 8. np.cumsum & np.cumprod

print(np.cumsum(b))
print(np.cumsum(a,axis=0))
print()
print(np.cumprod(b))
print(np.cumprod(a,axis=1))
print()