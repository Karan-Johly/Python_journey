def recursion_table(n,m=0): 
    if m>10:
        return 1
    print("%d X %d = %d"%(n,m,n*m))
    recursion_table(n,m+1)
    return ("Table of %d Printed."%n)

n=int(input("Enter the Number:"))
print(recursion_table(n))