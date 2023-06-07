#  Write a Python program to count occurrences of a substring in a string.

str="dadadadadad"
sub_str="dada"

count=sum(1 for i in range(len(str))if str.startswith("dada", i))
print("occurence of sub string is : ", count)

# string = input("Enter a string : ")
# substring = input("Enter a substring : ")

# count = string.count(substring)

# print("substring occurs times", count)