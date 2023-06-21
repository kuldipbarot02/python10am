# Write a Python program to count occurrences of a substring in a string
# my_string=input("Enter a string : ")
# my_substring=input("Enter a substring :")

# my_count=my_string.count(my_substring)

# print("Substirng occuurs %d times" % my_count)

str="dadadadadad"
sub_str="dadada"

count=sum(1 for i in range(len(str))if str.startswith("dada", i))
print("occurence of sub string is : ", count)

# string = input("Enter a string : ") 
# substring = input("Enter a substring : ")

# count = string.count(substring)

# print("substring occurs times", count)