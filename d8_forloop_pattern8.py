n=int(input("Enter the Value: "))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#          if(row==col):
#                 print("$",end=' ')
#          elif(row==1 or row==n) or (row+col==row+1 or row+col==row+n):
#             print("*",end=' ')
#          else:
#             print(" ",end=' ')
#     print()
































# print()
# print("*******NEXT PATTERN*******")
# print()
for row in range(1,n+1):
    for col in range(1,n+1):
         if(row==col) or (row+col==6):
                print("$",end=' ')
         elif(row==1 or row==5) or (row+col==row+1 or row+col==row+5):
            print("*",end=' ')
         else:
            print(" ",end=' ')
    print()
