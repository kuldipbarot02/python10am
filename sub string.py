#  Write a Python program to count occurrences of a substring in a string.

str="dadadadadad"
sub_str="dadada"

count=sum(1 for i in range(len(str))if str.startswith("dadada", i))
print("occurence of sub string is : ", count)

# string = input("Enter a string : ") 
# substring = input("Enter a substring : ")

# count = string.count(substring)

# print("substring occurs times", count)