#%%

#16. Given new_array from the last exercise, and the code x = new_array, you run the code:

import numpy as np

new_array = np.array([[ 1,  2,  3,  4],
                    [ 5,  6,  7,  8],
                    [ 9, 10, 11, 12]])

x = new_array
x[0,0] = 42
print(x[0,0])
print(new_array[0,0])

#Following this code, what is displayed?
#This displayed is 42 and 42, because both arrays are conecting

#If you need make a "copy" of originally array, use this code:
x = new_array.copy()