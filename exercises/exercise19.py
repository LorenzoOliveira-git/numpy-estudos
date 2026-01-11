#%%

#19. Given this code:

import numpy as np

z_list = [z for z in range(0,5)]
y_list = [z_list for y in range(0,4)]
x_list = [y_list for x in range(0,3)]

x_array = np.array(x_list)

#What would the value of x_array.shape be?
#The value will be shape=(3,4,5)

x_array.shape
# %%
