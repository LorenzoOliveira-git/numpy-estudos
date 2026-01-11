#%%

import numpy as np

#It's the same idea of pandas.
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

c = a[a > 5].reshape((2,2))
print(c)
print(type(c))
# %%
