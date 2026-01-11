#%%

#33. For NumPy arrays, logical operations are done with the operators “&” and “|”, rather than the usual Python “and” and “or”. Given that, what would be the result of this expression?
#(one_dim > 4) | (one_dim == 1)

import numpy as np
from variable_exercise29_to_36 import one_dim

#The expression result is [True,False,False,False,True]

print((one_dim > 4)|(one_dim == 1))
# %%
