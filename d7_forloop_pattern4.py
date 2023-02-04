n=3
for i in range(n):
    for k in range(i):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()