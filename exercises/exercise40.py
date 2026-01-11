#%%

#40. Assuming you saved the file, “data.npz”, in #38, how could you reload the arrays into two new variables: people2 and languages2?

import numpy as np

people2 = np.load("data.npz")["people"]
languages2 = np.load("data.npz")["languages"]

print("people2 = "+str(people2)+"\nlanguages2 = "+str(languages2))
# %%
