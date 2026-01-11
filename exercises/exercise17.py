#%%

#17. How could you create a two-dimensional, 3 x 4 array (three arrays of four elements each) with random numbers from 1 to 10?

import numpy as np
from numpy.random import default_rng

rng=default_rng()

array = rng.integers(1,10,size=(3,4),endpoint=True)
print(array)
# %%
