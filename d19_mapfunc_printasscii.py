def asscii_values(a):
    return ord(a)

l1=['a','A','v','B','m','o']
result=map(asscii_values,l1)
print(l1)
print(list(result))