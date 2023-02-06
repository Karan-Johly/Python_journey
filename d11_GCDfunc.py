def GCD(x,y):
    rem=x%y
    if(rem==0):
        return y
    else:
        return GCD(y,rem)

n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
print("The GCD of numbers is",GCD(n,m))