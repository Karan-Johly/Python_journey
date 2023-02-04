mark1 = float(input("enter the marks in maths : "))
mark2 = float(input("enter the marks in science : "))
mark3 = float(input("enter the marks in punjbai : "))
mark4 = float(input("enter the marks in sst : "))
total = float(mark1 + mark2 + mark3 + mark4)
avg = float(total/4)
print("total marks in obtain in class is %f "%total)
print("percentage obtain is %f"%avg)
if(avg>75):
  print("distinction")
elif(avg>=60 and avg<75):
  print("first divison")
elif(avg>=50 and avg<60):
  print("second division")
elif(avg>=40 and avg<50):
  print("third division")
else:
  print("work hard !! YOU ARE FAIL.......")