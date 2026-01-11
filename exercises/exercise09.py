#%%

#9. How could you create a ten-element array of random integers between 1 and 5 (inclusive)?

import numpy as np
from numpy.random import default_rng

rng=default_rng()

array_random = rng.integers(1,5,size=10,endpoint=True)
print(array_random)
# %%
