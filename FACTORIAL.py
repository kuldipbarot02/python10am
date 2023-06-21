# Write a Python program to get the Factorial number of given number

N=int(input("Enter N : "))
fac=1

for i in range(1,N+1):
    fac=fac*i
    print("fac of n is : ",fac)
