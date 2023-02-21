import numpy as np
#Working on 1D
# inp_arr = np.arange(5)
# print("arr value: \n", inp_arr)
# print("Shape: ", inp_arr.shape)
# # deletion 1D array 
# object = 2
# a = np.delete(inp_arr, object)
# print("\nDeleteing arr value at 2: ", a)
# print("Shape: ", a.shape)
arr = np.arange(9).reshape(3, 3)
print("arr value: ", arr)
print("Shape : ", arr.shape,'\n')
# deletion from 2D array 
val = np.delete(arr, 1, 0)
print("Deleting arr value 2 times : \n", val)
print("Shape : ", val.shape)
# deletion from 2D array 
val = np.delete(arr, 1, 1)
print("\ndelteing arr value 2 times : \n", val)
print("Shape : ", val.shape)