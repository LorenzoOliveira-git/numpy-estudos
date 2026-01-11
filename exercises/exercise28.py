#%%

#28. Write an expression to return the last two columns of the middle two rows.

import numpy as np
from variable_exercise22_to_28 import four_by_five

print(four_by_five[1: four_by_five.shape[0] -1,-2:])
# %%
