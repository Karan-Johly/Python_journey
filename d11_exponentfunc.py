def exp(x,y):
    if y==0:
        return 1
    else:
        return x*exp(x,y-1)

x=int(input("Enter Number: "))
y=int(input("Enter power for the above Number: "))

print(exp(x,y))