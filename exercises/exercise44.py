#%%

#44. How could you surround each string with an initial and final asterisk character (*)?

import numpy as np
from variable_lumberjack import lumberjack

arr1 = np.char.add(["*"],lumberjack)
arr2 = np.char.add(arr1,["*"])

print(arr2)
# %%
