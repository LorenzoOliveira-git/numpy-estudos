#%%

#30. What would be returned by this expression: one_dim + np.arange(5, 0, -1) ?

import numpy as np
from variable_exercise29_to_36 import one_dim

#This expression returns one array likes that [6,6,6,6,6], bacause the one_dim is [1,2,3,4,5] and np.arange(5,0,-1) is [5,4,3,2,1]

print(one_dim + np.arange(5,0,-1))
# %%
