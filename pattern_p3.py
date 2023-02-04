n=int(input("Enter the Value: "))
for i in range(n):
    for j in range(n,i,-1):
        print("*",end=' ')
    print()