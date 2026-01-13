#%%

#42. Given the CSV file saved in #41, how could you load it back into a variable, arr2?

import numpy as np

arr2 = np.genfromtxt('myarray.csv',delimiter=',')
print(arr2.dtype)

# %%
