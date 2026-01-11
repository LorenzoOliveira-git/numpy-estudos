#%%

import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)
#%%

#OPERATIONS - obs: all methods make a new matrix
#minus
c = a - b
print(c)
# %%

#plus with two vectors
d = a + b
d
#plus in the own vector
d = a.sum()
d

# %%

#exponential
b**2

# %%

#multiplication OBS: sin calculated the sine of numbers
10 * np.sin(a)

# %%

#Validation
30 < a

# %%

#OBS: The multiplication * is callled for "element-wise product", because its operation multiplicate value to value in both arrays, for example:
a = np.array([[3,4],
             [2,4]])
b = np.array([[1,2],
             [1,2]])
a * b
#Result: [3,8]
#        [2,8]
#Because it mulplicates both values in the same index

#But, if you want the mulplicate matrix, use this method
a.dot(b)
#or
a @ b
#This method is called "dot", because the name of operation is "dot product". They function equals in matrix, so, your number of columns (first matrix) have to be equals with its number of lines (second matrix).

# %%

from numpy.random import default_rng
#+= and -=
#OBS: the method "default_rng" make a limite that random values can reach
a = np.ones((2,3),dtype=int)
rng=default_rng()
b = rng.random()

a*=3
print(a)

b += a
print(b)

#a += b
#print(a)
#it don't work because the numpy don't convert both values for to unique type, you need change one their.
a.dtype = float
a += b
print(a)
# %%

#methods statistics
print(a.max())
print(a.min())
print(a.std())
print(a.mean())

#OBS:generate random values
rng.integers(low=10,high=100,size=5)
rng.standard_normal(10)

# %%
