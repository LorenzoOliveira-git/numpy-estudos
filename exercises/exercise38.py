#%%

#38. For the defined above in #36, what are the values for:
import numpy as np
arr = np.array([0., .5, 1.0, 1.5, 2.0]) * np.pi
np.around(np.cos(arr), 0)

# The value is [1., 0., -1, -0., 1.]
# %%
