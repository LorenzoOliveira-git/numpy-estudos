#%%

import numpy as np
#For you print an array in numpy, you use the comand "print"
array = np.arange(10).reshape(2,5)
print(array)
# %%

#If you have an array with a lot of data, it'll hide a lot of data in your array.
zeros = np.zeros([100,100])
print(zeros)

# %%

#If you don't want this behaviour, use this comand:
import sys
np.set_printoptions(threshold=sys.maxsize)
print(zeros)

# %%
