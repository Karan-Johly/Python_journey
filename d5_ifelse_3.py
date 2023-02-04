n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))

if(n1<n2 and n1<n3):
    print("%d is smaller from %d and %d."%(n1,n2,n3))
elif(n2<n1 and n2<n3):
    print("%d is smaller from %d and %d."%(n2,n1,n3))
else:
    print("%d is smaller from %d and %d."%(n3,n1,n2))