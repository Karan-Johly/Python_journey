def table(n):
    for i in range(1,11,1):
        print("%d X %d = %d"%(n,i,n*i))
num=int(input("Enter the Number: "))
table(num)