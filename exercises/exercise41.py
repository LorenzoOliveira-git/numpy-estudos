#%%

#41. Given

import numpy as np

arr = np.arange(1,13).reshape(3,4)
print(arr)

# How could you save it to a CSV file, “myrray.csv”.

np.savetxt("myarray.csv",arr,delimiter=',')

# %%
