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

# 9. np.percentile

print(np.percentile(b,100))
print(np.percentile(b,0))
print(np.percentile(b,50))
print()

# 10. np.histogram

print(np.histogram([0,10,20,30,40,50,60,70,80,90,100]))
print()

# 11. np.corrcoef

salary = np.array([20000,25000,30000,45000,50000,65000])
exp = np.array([1,2,3,5,2,4])
print(np.corrcoef(salary,exp))
print()

# 12. np.isin()

items = [14,7,39,40,57]
print(np.isin(a,items))
print(a[np.isin(a,items)])
print()

# 13. np.flip()

print(np.flip(b))
print(np.flip(a,axis=1))
print()

# 14. np.put()

np.put(b,[0,2],[113,1000])
print(b)
print()

# 15. np.delete()

print(np.delete(b, 0))
print(np.delete(b, [1,3,5]))
print()

# 16. np.clip()

print(np.clip(b,25,75))
print()

# Set Functions

m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])
print(np.union1d(m,n))
print()
print(np.intersect1d(m,n))
print()
print(np.setdiff1d(m,n))
print()
print(np.setxor1d(m,n))
print()