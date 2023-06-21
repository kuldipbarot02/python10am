# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))

a+b+c
if(a==b or b==c or c==a):
    print("sum will be zero")
else:
    print(sum)