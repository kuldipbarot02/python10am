# 1 Function with no argument & no return value.

def printline ():
    print("*"*50)
# printline()
# print("welcome to user defined function in python.")
# printline()

# 2. Funtion with argument but not Return value.

def add(a,b):
    print("Addition :", a+b)

printline()
x=int(input("Enter value :"))
y=int(input("Enter value :"))
add(x,y)
printline()

# 3. Function with argument & with Retuen value.

def sub(a,b):
    return  a-b
printline()
x=int(input("Enter value : "))
y=int(input("Enter value : "))
# ans=sub(x,y)
print("subtraction :",sub(x,y))
printline()

