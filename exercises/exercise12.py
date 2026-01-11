#%%

#12. Consider the code: np.ones((3,5)). Does this 
# A) create an array of three arrays containing five elements each or 
# B) create an array of five arrays containing three elements each?

#Letter A, because the first parameter is the number of rows, and the second paramter is the number of columns
import numpy as np

ones = np.ones((3,5))
print(ones)
# %%
