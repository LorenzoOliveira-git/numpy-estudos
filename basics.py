#%%

import numpy as np

#Attibutes of numpy arrays

#Number of dimension
np.ndarray.ndim

#Number of line and columns in a numpy array, represented for (n,m), n = rows m = columns
np.ndarray.shape

#Type of data in numpy array
np.ndarray.dtype

#Size of type data in numpy array, in other words, if you have the type int64, the result is 8, because the attribute gets the number of bytes (64) and divite to 4.
np.ndarray.itemsize

#Size of array
np.ndarray.size

# %%

#let's make a new array - this is the simple array, but you type it's ndarray
array1 = np.array([1,2,3])
type(array1)

# %%

#Let's make a new array with more than dimension
array2 = np.array([(1,2,3),(1,3,4)])
array2

# %%

#You can especific the array's data type in onw method
array3 = np.array([[1,2,3],[4,5,6]],dtype=np.complex128)
array3

# %%

#You can make null matriz (matriz only zeros), indentity matrix (matriz only ones) 
zeros = np.zeros([5,5])
zeros
ones = np.ones([5,5])
ones
#The default type data is float64, if you change the type, you have to use the parameter dtype=

# %%

#If you need the array with one sequence of numers, use the method arange, the first argument is the number initial value, the second number is the end value and the third value is of how much in how much it will jump.
sequence = np.arange(3,4,0.2)

#But, if you want a specific number of data in you array, use this method: (The third parameter is the number of data that you need)
sequence = np.linspace(0,2,40)
