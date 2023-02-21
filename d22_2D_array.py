import numpy as np
arr2d=[]
r=int(input("Enter the number of Rows: "))
c=int(input("Enter the number of Columns: "))
for i in range(r):
    a=[]
    for j in range(c):
        val=int(input("Enter the value at [%d,%d]"%(i,j)))
        a.append(val)
    arr2d.append(a)
arr2d=np.array(arr2d)
for i in range(r):
    for j in range(c):
        print(arr2d[i][j])
print(arr2d)
