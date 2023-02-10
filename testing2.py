dict={0:33,1:33,2:78,3:89,4:65,5:33}
print(dict)
for i in range(5):
    for j in range(5):
        if dict[i-1] == dict[j-1]:
            r=dict.pop(i)
            print(r)
print(dict)