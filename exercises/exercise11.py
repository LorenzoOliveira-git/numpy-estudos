#%%

#11. What code would create an array of 10 random numbers between zero and one?

import numpy as np
from numpy.random import default_rng

rng=default_rng()

random_array = rng.random(10)
print(random_array)


# %%
