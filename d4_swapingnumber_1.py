num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))

print("\n***Before Swaping***")
print("First Number : ",num1)
print("Second Number : ",num2)

num2=num2+num1
num1=num2-num1
num2=num2-num1

print("\n***After Swaping***")
print("First Number : ",num1)
print("Second Number : ",num2)