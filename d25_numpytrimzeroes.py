import numpy as np
arr=np.array([0,0,1,0,2,0,0,0,35,7,0,0,0,21,33,0,0,0])
trm=np.trim_zeros(arr,trim='fb')
print(trm)