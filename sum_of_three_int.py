Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

a=int(input("Enter n : "))
b=int(input("Enter n : "))
c=int(input("Enter n : "))
sum=a+b+c
if(a==b or b==c or c==a):
    print("Sum will be zero")

else:
    print(sum)

