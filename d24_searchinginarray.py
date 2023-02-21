import numpy as np
# where function
arr=np.array([10,20,30,40,50,40,60,40])
print(np.where(arr==40))
# searchsorted function
print(np.searchsorted(arr,35))
print(np.searchsorted(arr,35,side='right'))
