#%%

#4. How might you create a NumPy array of the capital letters, A-Z?

import numpy as np
import string

alphabet = string.ascii_uppercase

array = np.array(list(alphabet))
print(array)

#or

first_letter = ord("A")
final_letter = ord("Z") + 1
#I need put this "+ 1", because for I interate and get the letter corresponding with number, the letter "Z" needs to be in the count.
array_number = np.arange(first_letter,final_letter)
array_letter = np.array([chr(i) for i in array_number ])
print(array_letter)
# %%
