def fiboseries(n):
    if n<2:
        return 1
    return fiboseries(n-1)+fiboseries(n-2)
n=int(input("Enter the number terms for fibonacci series: "))
for i in range(n):
    print("Fibonacci(",i,")= ",fiboseries(i))