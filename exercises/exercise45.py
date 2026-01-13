#%%

#45. The function, np.where, can be used to create an array of indexes that can be used to index into the original array to subset an array based on a condition. If passed only a condition, it returns a set that array in the first value of a tuple, and we need to ignore the second (empty) condition. We can then use the indexes returned to get an array of the elements themselves.

#Given that background, what might you expect the following to display?

import numpy as np
from variable_lumberjack import lumberjack

search_results, = np.where(np.char.str_len(lumberjack) >=5)
print(search_results)
print(lumberjack[search_results])

#The result is 
# [2 7 9]
# ['lumberjack' 'sleep' 'night']
# %%
