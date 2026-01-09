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

#plus
d = a + b
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

#+= and -=
#OBS: the method "default_rng" make a limite that random values can reach
a = np.ones((2,3),dtype=int)
b = np.random.random((2,3))

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
