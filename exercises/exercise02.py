#%%
#How could you create the same NumPy array using a Python range and a list?

import numpy as np

list_to_array = [i for i in range(10,100,10)]
array = np.array(list_to_array)
print(array)
# %%
