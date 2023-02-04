from array import *
ar1=array('u',['a','c','d','e'])
ch=input("Enter the character: ")
pos=int(input("Enter the position: "))
ar1.insert(pos,ch)
for x in ar1:
    print(x)
pos=int(input("Enter the position of the element you want to delete: "))
ar1.pop(pos)
for x in ar1:
    print(x,end=' ')


