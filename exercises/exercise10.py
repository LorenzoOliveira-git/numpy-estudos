#%%

#10. How can you create a normal distribution of 10 numbers, centered on 5?

import numpy as np
from numpy.random import default_rng

rng=default_rng()

array_normal_distribution = rng.normal(loc=5, size=10)
print(array_normal_distribution)
# %%
