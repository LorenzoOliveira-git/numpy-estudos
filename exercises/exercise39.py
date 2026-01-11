#%%

#39. You’re asked to save the following two arrays as is to a file, “data.npz”. The arrays should be named as they are here in the file. How could you do it?

import numpy as np
people = np.array(["John", "Jennifer", "Helen", "Miryam"])
languages = np.array([2, 2, 1, 1])

np.savez("data.npz",people=people,languages=languages)
# %%
