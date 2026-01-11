#%%

#Break out those pictures of the unit circle for this one, for some trigonometry so simple an ex-history major can do it – well at least (menos) I can on a good day.

#As background, we can round numbers to a decimal precision using np.around(arr, num_decimals), and get the sine of an angle (in radians) using np.sin. So with that, given the following array of angles in radians:

import numpy as np

arr = np.array([0., .5, 1.0, 1.5, 2.0]) * np.pi

#What does the following display:

print(np.int32(np.sin(arr)))

#Note: the fact that we’re able to cast to an integer is a bit of a hint, but otherwise, we can end up with some pretty surprising rounding errors!
# %%

#The result value is [0 1 0 -1 0]