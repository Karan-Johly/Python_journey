import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(np.diag(np.diag(arr)))
arr=np.flip(arr,axis=0)
arr=np.flip(np.diag(np.diag(arr)),axis=0)
print(arr)