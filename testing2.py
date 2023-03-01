# f=open('main.txt','r+')
a='The Quick Brown Fox jumped'
# leng=len(a)
for i in range(len(a)):
    if ((ord(a[i])>=65) and (ord(a[i])<=90)):
        print(a[i])

# f.write(a)
# c=f.read()

