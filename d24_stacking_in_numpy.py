import numpy as np
# 1-D array stacking
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
# Horizontal Stacking
print(np.hstack((a,b)))
print()
# Vertical Stacking
print(np.vstack((a,b)))

# 2-D array stacking
np.random.seed(1)
arr1=np.random.randint(1,33,9).reshape(3,3)
arr2=np.random.randint(43,73,9).reshape(3,3)
print(arr1)
print(arr2)
# Horizontal Stacking
print(np.hstack((arr1,arr2)))
print()
# Vertical Stacking
print(np.vstack((arr1,arr2)))