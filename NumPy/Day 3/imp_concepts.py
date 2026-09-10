import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# Indexing and Slicing

# for 1d
print("a1:-")
print(a1)
print(a1[2])

# for 2d
print("a2:-")
print(a2)
print(a2[1,2])
print(a2[2,1])
print(a2[1,3])


# for 3d
print("a3:-")
print(a3)
print(a3[1,0,1])
print(a3[1,1,0])
print(a3[0,1,0])

print("------------------------------------")

# Slicing

# for 1d
print("a1:-")
print(a1)
print(a1[2:8:2])
print(a1[-1::-1])

# for 2d
print("a2:-")
print(a2)
print(a2[0:])
print(a2[:,2])
print(a2[1:,1:3])
print(a2[::2,::3])
print(a2[1::,1::2])
print(a2[::2,1::2])
print(a2[1:2,::3])
print(a2[0:2,1::])

# for 3d

a3 = np.arange(27).reshape(3,3,3)
print("a3:-")
print(a3)
print(a3[1])
print(a3[0])
print(a3[0,1:2,0:])
print(a3[1,:,1])
print(a3[2,1:,1:])
print(a3[::2,0,::2])

print("----------------------------------------")

# iteration

print("for 1d array :-")
for i in a1 :
    print(i)
print("for 2d array :-")
for i in a2 :
    print(i)
print("for 3d array :-")
for i in a3 :
    print(i)

# np.nditer()

print("for 2d array :-")
for i in np.nditer(a2):
    print(i,end=" ")

print("\nfor 3d array :-")
for i in np.nditer(a3):
    print(i, end=" ")

print()
print("----------------------------------")

# Reshaping

# np.transpose

print(np.transpose(a2))
print(np.transpose(a3))
print(np.transpose(a1))

# or 

print(a2.T)

# array.ravel()

print(a2.ravel())
print(a3.ravel())

print("-----------------------------------")


# stacking

b1 = np.arange(12).reshape(3,4)
b2 = np.arange(12,24).reshape(3,4)

# hstack
print(np.hstack((b1,b2)))

# vstack
print(np.vstack((b1,b2)))
print(np.vstack((b1,b2,b1)))

print("--------------------------------------")


# splitting
# np.hsplit

print(np.hsplit(b1,2))
print(np.hsplit(b1,4))

# np.vsplit

print(np.vsplit(b2,3))

print("-------------------------------------")


