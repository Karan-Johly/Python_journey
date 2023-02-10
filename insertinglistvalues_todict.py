n=int(input("Enter the number of values you want: "))
lis=[]
for i in range(n):
    v=input("Enter the value: ")
    lis.append(v)
dict={k:v for k,v in enumerate(lis)}
print(dict)