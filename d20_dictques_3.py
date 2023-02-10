n=int(input("Enter the number of values you want: "))
lis=[]
for i in range(n):
    v=input("Enter the value: ")
    lis.append(v)
dict={k:v for k,v in enumerate(lis)}
# d={"Name":"Karan","Class":"IT","Rollno":33,"Name2":"Karan"}

print(dict)
temp={}
for i in range(n):
    if dict[i] not in temp.values():
        temp[i]=dict[i]
dict=temp
print(dict)