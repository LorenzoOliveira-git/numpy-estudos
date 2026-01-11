#%%

#20. Given x_array from #19, what is the value for x_array.ndim?

import numpy as np

z_list = [z for z in range(0,5)]
y_list = [z_list for y in range(0,4)]
x_list = [y_list for x in range(0,3)]

x_array = np.array(x_list)

#The value of x_array.ndim is three, because this tensor has 3 dimensions
