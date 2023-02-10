dict={0:23,1:239,2:23}
print(dict)
if dict.get(0,None)==dict.get(2,None):
    dict.pop(0,None)

print(dict)

if dict.get(0,None)==dict.get(2,None):
    dict.pop(0,None)
print(dict)