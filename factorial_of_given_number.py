# Write a Python program to get the Factorial number of given number.

n=int(input("Enter a number : "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print("fac of n is : ", fac)