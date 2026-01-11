#%%

#13. Consider an array named “myarray” that is displayed as in the block below. What value does the code myarray[1,2] return? A) 10 B) 7.

import numpy as np

myarray = np.array([[ 1,  2,  3,  4],
                    [ 5,  6,  7,  8],
                    [ 9, 10, 11, 12]])

#The result of myarray[1,2] is "7", because the first parameter is the row index and the second parameter is the column index

print(myarray[1,2])
# %%
