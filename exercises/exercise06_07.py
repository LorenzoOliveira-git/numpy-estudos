#%%

#6. How would you find the data type given in #4.
#7. What is the data type for #4?

#6.
import numpy as np
import string

alphabet = string.ascii_uppercase

array = np.array(list(alphabet))
print(array)

array.dtype

#7.
#The type of array in exercise 4 is '<U1'
# %%
