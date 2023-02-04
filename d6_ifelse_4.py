n1=int(input("Enter First number: "))
n2=int(input("Enter Second number: "))
n3=int(input("Enter Third number: "))

if(n1>n2):
    if(n1>n3):
        print("%d is greater than %d and %d"%(n1,n2,n3))
if(n2>n1):
    if(n2>n3):
        print("%d is greater than %d and %d"%(n2,n1,n3))
if(n3>n1):
    if(n3>n2):
        print("%d is greater than %d and %d"%(n3,n2,n1))
