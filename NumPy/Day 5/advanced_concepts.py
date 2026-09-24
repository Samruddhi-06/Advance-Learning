import numpy as np

# Broadcasting

a = np.arange(12).reshape(4,3)
b = np.arange(3)
print(a+b)
print()
print(a-b)
print()

x = np.arange(12,24).reshape(3,4)
y = np.arange(4).reshape(1,4)
print(x+y)
print()

# working with mathematical formulas

# 1. sigmoid

def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

a1 = np.arange(10)
print(sigmoid(a))
print()

# 2. mean squared error

def mse(actual,predicted):
    return np.mean((actual - predicted)**2)

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

print("Mean Square Error:",mse(actual,predicted))
print()

# 3. Binary cross entropy

def bce(act,pred):
    epsilon = 1e-15
    pred = np.clip(pred, epsilon, 1-epsilon)

    loss = -np.mean(act* np.log(pred) + (1 - act)* np.log(1 - pred))
    return loss

act = np.array([0,1,0,1,0])
pred = np.array([0.9,0.5,0.2,0.05,0.1])
print("BCE:",bce(act,pred))
print()

# working with missing values

a2 = np.array([1,2,3,4,np.nan,6]).reshape(2,3)
l1 = a2[~np.isnan(a2)]
print(l1)

# Ploting graphs
# 1. x = y

import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = x
plt.plot(x,y)
plt.show()

# 2. y = x^2

y = x**2
plt.plot(x,y)
plt.show()

# 3. y = sinx

y = np.sin(x)
plt.plot(x,y)
plt.show()

# 4. y = xlogx

y = x * np.log(x)
plt.plot(x,y)
plt.show()

# 5. sigmoid

y = 1/(1 + np.exp(-x))
plt.plot(x,y)
plt.show()