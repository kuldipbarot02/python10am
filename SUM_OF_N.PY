# Write a python program to sum of the first n positive integers.
n=int(input("Enter n : "))

sum=0
for i in range(n+1):
    sum=sum+i
print("sum of n is : ", sum)