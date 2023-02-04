n=int(input("Enter the Value: "))
for num in range(0,n,3):
    print("%d,"%2**num,end=' ')
print()
for i in range(-1,5,1):
    if(i==-1):
        print("-5, -2, ",end='')
    else:
        print("%d,"%(i*3),end=' ')
print()
for j in range(-1,-7,-1):
    print("%d,"%(j*2),end=' ')
print()
for k in range(1,11,3):
    print("%d,"%k,end=' ')