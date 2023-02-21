import numpy as np
inp_arr = np.array([[11,12,13],[14,15,16]])
print ('Input array:')
print (inp_arr )
print ('\nAppending the elements to array:')
print (np.append(inp_arr,[[17,18,19]],axis=0))
# print (np.append(inp_arr,[[17,18,19]],axis=1))
print (np.append(inp_arr,[[17,18,19],[20,21,22]],axis=1))