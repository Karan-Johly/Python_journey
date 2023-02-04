n=int(input("Enter your Value: "))
for i in range(n):
    for j in range(i):
        print(" ",end=' ')
    for l in range(n,i,-1):
        print("*",end=' ')
    for k in range(n,i+1,-1):
        print("*",end=' ')
    print()