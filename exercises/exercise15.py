#%%

#15. An array of three arrays of four elements each like this has twelve elements, of course. How could you create a new array consisting of two arrays of six elements each?

import numpy as np
array = np.arange(1,13).reshape(2,6)
print(array)
# %%
