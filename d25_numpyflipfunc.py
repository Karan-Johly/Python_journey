import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# print(np.flip(arr))
arr_2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d)
print(np.flip(arr_2d))
print(np.flip(arr_2d,axis=0))
print(np.flip(arr_2d,axis=1))