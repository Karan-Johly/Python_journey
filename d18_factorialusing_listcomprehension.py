no=int(input("Enter the range for Factorial: "))
# f=1
# f=[f:=f*val for val in range(no,1,-1)]

# print(f)

f=[1]
f=[f[-1] for i in range(1,no+1) if not f.append(i*f[-1])]
print(f[-1])