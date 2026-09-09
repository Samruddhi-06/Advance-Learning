import numpy as np

a1 = np.arange(15,27).reshape(3,4)
print("a1 :-",a1.astype(int))
a2 = np.random.random((3,4)) * 100
print("a2 :- ",a2.astype(int))

print("------------------")

# Changing datatype

print(a1.astype(np.float32))

print("------------------")

# Array Operations

# Scalar operations
# arithmatic

print("add :-",a1 + 10)
print("sub :-",a1 - 10)
print("mul :-",a1 * 10)
print("div :-",a1 / 10)
print("expo :-",a1 ** 10)
print("mod :-",a1 % 10)

print("------------------")

# relational

print("a2 > 23 :- ", a2 >3)
print("a2 < 55 :- ", a2 <3)
print("a2 >= 63 :- ", a2 >=3)
print("a2 <= 3 :- ", a2 <=3)
print("a2 != 41 :- ", a2 !=3)
print("a2 == 15 :- ", a2 ==3)

print("------------------")


# vector operations

print("a1 * a2",a1 * a2)
print("a1 + a2",a1 + a2)
print("a1 / a2",a1 / a2)
print("a1 - a2",a1 - a2)

print("------------------")

# Array functions

# min,max,sum,prod

print(np.max(a1))
print(np.max(a1,axis=0))
print(np.min(a1))
print(np.min(a1, axis=1))
print(np.sum(a1))
print(np.sum(a1, axis=0))
print(np.prod(a1))
print(np.prod(a1, axis=1))

print("------------------")

# mean,median,std,var

print(np.mean(a2))
print(np.mean(a2,axis=1))
print(np.median(a2))
print(np.median(a2,axis = 0))
print(np.std(a2))
print(np.std(a2,axis=1))
print(np.var(a2))
print(np.var(a2, axis=0))

print("------------------")

# trigonometric function

print("sin(a1) :-",np.sin(a1))
print("cos(a1) :-",np.cos(a1))
print("tan(a1) :-",np.tan(a1))

print("------------------")

# dot product

a3 = np.random.random((4,3))*100
print(a3.astype(int))

print("dot product of a1 and a3 :-")
print(np.dot(a1,a3))

print("------------------")

# log and exponent

print(np.log(a1))
print(np.exp(a3))

print("------------------")

# round, floor, ceil

print("a2 :-",a2,"\nRound :-",np.round(a2))
print("a2 :-",a2,"\nFloor :-",np.floor(a2))
print("a2 :-",a2,"\nCeil :-",np.ceil(a2))

print("------------------")

