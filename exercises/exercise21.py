#%%

#21. Given an array, named "arr”, that looks like:
import numpy as np

arr = np.array([[0, 1, 2],
       [3, 4, 5]])

#How could you display an array that looks like:

#[[0, 3],
# [1, 4],
# [2, 5]]

print(arr.transpose())
# %%
