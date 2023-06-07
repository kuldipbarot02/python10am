# Write a Python program to get the Fibonacci series of given range.
# 0 1 1 2 3 5 8 13 21 34 

a,b=0,1
n=int(input("Enter n : "))

while b<n:
    print(b,end=" ")
    a,b=b,a+b
