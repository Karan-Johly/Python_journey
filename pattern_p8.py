n=int(input("Enter the Value: "))
for i in range(0,n):
    for j in range(n,i,-1):
        print(" ",end=' ')
    for l in range(i):
        print("*",end=' ')
    for k in range(i+1):
        print("*",end=' ')
    print()